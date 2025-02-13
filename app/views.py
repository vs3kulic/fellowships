from django.shortcuts import render, get_object_or_404, redirect
from .models import Character, BattleOutcome
import random

def index(request):
    characters = Character.objects.filter(is_main_character=True)
    return render(request, 'index.html', {'characters': characters})

def select_character(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    if character.is_main_character:
        character.fetch_and_assign_quotes()  # Fetch and assign quotes only for main characters
    request.session['selected_character_id'] = character.id  # Store the selected character's ID in the session
    return render(request, 'select_character.html', {'character': character})

def opponent_selected(request):
    opponent = Character.objects.filter(is_antagonist=True).order_by('?').first()
    request.session['opponent_id'] = opponent.id  # Store the opponent's ID in the session
    message = "You have selected an opponent."
    return render(request, 'opponent_selected.html', {'character': opponent, 'message': message})

def coin_toss(request):
    if request.method == 'POST':
        user_choice = request.POST.get('coin_choice')
        coin_result = random.choice(['heads', 'tails'])
        result = 'win' if user_choice == coin_result else 'lose'
        return redirect('coin_toss_result', result=result)
    return render(request, 'coin_toss.html')

def coin_toss_result(request, result):
    return render(request, 'coin_toss_result.html', {'result': result})

def battle(request):
    selected_character_id = request.session.get('selected_character_id')
    opponent_id = request.session.get('opponent_id')
    main_character = get_object_or_404(Character, id=selected_character_id)
    opponent = get_object_or_404(Character, id=opponent_id)
    coin_toss_result = request.POST.get('coin_toss_result')

    steps = []
    first_attacker = main_character if coin_toss_result == 'win' else opponent
    second_attacker = opponent if first_attacker == main_character else main_character

    while main_character.life_points > 0 and opponent.life_points > 0:
        # First attacker attacks
        damage = first_attacker.attack(second_attacker)
        steps.append(f"{first_attacker.name} attacks {second_attacker.name} and deals {damage} damage.")
        if second_attacker.life_points <= 0:
            steps.append(f"{second_attacker.name} is defeated!")
            outcome = 'Win' if first_attacker == main_character else 'Loss'
            BattleOutcome.objects.create(player=main_character, opponent=opponent, outcome=outcome)
            break

        # Second attacker attacks
        damage = second_attacker.attack(first_attacker)
        steps.append(f"{second_attacker.name} attacks {first_attacker.name} and deals {damage} damage.")
        if first_attacker.life_points <= 0:
            steps.append(f"{first_attacker.name} is defeated!")
            outcome = 'Loss' if first_attacker == main_character else 'Win'
            BattleOutcome.objects.create(player=main_character, opponent=opponent, outcome=outcome)
            break

    return render(request, 'battle.html', {'steps': steps})

def battle_results(request):
    selected_character_id = request.session.get('selected_character_id')
    character = get_object_or_404(Character, id=selected_character_id)
    outcomes = BattleOutcome.objects.filter(player=character).order_by('-timestamp')

    return render(request, 'battle_results.html', {
        'character_name': character.name,
        'outcomes': outcomes
    })
