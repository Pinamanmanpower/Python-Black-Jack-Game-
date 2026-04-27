import random
from loader import loading_animation


CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


def create_hand():
    return []


def draw_card(hand):
    card = random.choice(CARDS)
    hand.append(card)
    return hand


def deal_initial_cards(player_hand, dealer_hand):
    for _ in range(2):
        draw_card(player_hand)
        draw_card(dealer_hand)


def calculate_total(hand):
    total = sum(hand)

    while total > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        total = sum(hand)

    return total


def is_blackjack(hand):
    return len(hand) == 2 and calculate_total(hand) == 21


def show_player_hand(player_hand):
    print(f"\nYour hand: {player_hand} | Total: {calculate_total(player_hand)}")


def show_dealer_first_card(dealer_hand):
    print(f"Dealer shows: {dealer_hand[0]}")


def show_final_hands(player_hand, dealer_hand):
    print("\nFinal Hands")
    print(f"Player: {player_hand} | Total: {calculate_total(player_hand)}")
    print(f"Dealer: {dealer_hand} | Total: {calculate_total(dealer_hand)}")


def get_player_choice():
    valid_choices = ["h", "s"]

    while True:
        choice = input(
            "\nChoose your action:\n"
            "h = Hit\n"
            "s = Stand\n"
            "Enter choice: "
        ).lower()

        if choice in valid_choices:
            return choice

        print("Invalid choice. Please enter 'h' or 's'.")


def check_winner(player_hand, dealer_hand):
    player_total = calculate_total(player_hand)
    dealer_total = calculate_total(dealer_hand)

    if player_total > 21:
        print("You went bust. Dealer wins.")
    elif dealer_total > 21:
        print("Dealer went bust. You win.")
    elif player_total > dealer_total:
        print("You win.")
    elif player_total < dealer_total:
        print("Dealer wins.")
    else:
        print("Push. It is a draw.")


def play_blackjack():
    loading_animation(duration=3)

    player_hand = create_hand()
    dealer_hand = create_hand()

    deal_initial_cards(player_hand, dealer_hand)

    print("\nWelcome to Blackjack!")
    show_player_hand(player_hand)
    show_dealer_first_card(dealer_hand)

    if is_blackjack(player_hand) and is_blackjack(dealer_hand):
        show_final_hands(player_hand, dealer_hand)
        print("Both have blackjack. Push.")
        return

    if is_blackjack(player_hand):
        show_final_hands(player_hand, dealer_hand)
        print("Blackjack! You win.")
        return

    if is_blackjack(dealer_hand):
        show_final_hands(player_hand, dealer_hand)
        print("Dealer has blackjack. Dealer wins.")
        return

    while True:
        choice = get_player_choice()

        if choice == "h":
            draw_card(player_hand)
            show_player_hand(player_hand)

            if calculate_total(player_hand) > 21:
                show_final_hands(player_hand, dealer_hand)
                print("You went bust. Game over.")
                return

        elif choice == "s":
            print("\nYou stand. Dealer's turn.")

            while calculate_total(dealer_hand) < 17:
                draw_card(dealer_hand)
                print(f"Dealer draws: {dealer_hand} | Total: {calculate_total(dealer_hand)}")

            show_final_hands(player_hand, dealer_hand)
            check_winner(player_hand, dealer_hand)
            return


def play_again():
    while True:
        answer = input("\nDo you want to play again? (y/n): ").lower()

        if answer == "y":
            play_blackjack()
        elif answer == "n":
            print("Thanks for playing Blackjack.")
            break
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")


play_again()