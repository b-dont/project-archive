#include <iostream>
#include <array>
#include <algorithm>
#include <random>

enum class Face {
	Two, 		// 0
	Three, 	// 1
	Four, 	// 2
	Five, 	// 3
	Six, 		// 4
	Seven, 	// 5
	Eight,  // 6
	Nine,   // 7
	Ten,    // 8
	Jack,
	Queen,
	King,
	Ace,

	max_face
};

enum class Suit {
	Clubs,
	Diamonds,
	Hearts,
	Spades,

	max_suits

};

struct Card {

	Face face{};
	Suit suit{};
};

void printCard(const Card& card) {
	std::string valueCode{};
	std::string suitCode{};
	
	switch (card.face){
		case Face::Two:
			valueCode = "2";
			break;
		case Face::Three:
			valueCode = "3";
			break;
		case Face::Four:
			valueCode = "4";
			break;
		case Face::Five:
			valueCode = "5";
			break;
		case Face::Six:
			valueCode = "6";
			break;
		case Face::Seven:
			valueCode = "7";
			break;
		case Face::Eight:
			valueCode = "8";
			break;
		case Face::Nine:
			valueCode = "9";
			break;
		case Face::Ten:
			valueCode = "10";
			break;
		case Face::Jack:
			valueCode = "J";
			break;
		case Face::Queen:
			valueCode = "Q";
			break;
		case Face::King:
			valueCode = "K";
			break;
		case Face::Ace:
			valueCode = "A";
			break;
		default:
			valueCode = "?";
			break;

	}

	switch (card.suit) {
		case Suit::Clubs:
			suitCode = "♣";
			break;
		case Suit::Diamonds:
			suitCode = "♦";
			break;
		case Suit::Hearts:
			suitCode = "♥";
			break;
		case Suit::Spades:
			suitCode = "♠";
			break;
		default:
			suitCode = "?";
			break;
	}

	std::cout << valueCode << suitCode << ' ';
}

using Deck = std::array<Card, 52>;
using Hand = std::vector<Card>;

auto createDeck(){

	std::array<Card, 52> deck;
	int deckSize = 0;

	for (int face = 0; face < static_cast<int>(Face::max_face); ++face) {
		for (int suit = 0; suit < static_cast<int>(Suit::max_suits); ++suit) {
			deck[deckSize].face = static_cast<Face>(face);
			deck[deckSize].suit = static_cast<Suit>(suit);
			++deckSize;
		}
	}

	return deck;

}

void printDeck(const Deck& deck) { 

	for (auto card : deck) 
		printCard(card);
	
}

void printHand(const Hand& hand) { 

	for (auto card : hand) 
		printCard(card);
	
}

void shuffleDeck(Deck& deck) {
    // Hardware randomness
    std::random_device random_device;

    // Initialize PRNG (Pseudorandom Number Generator) using hardware entropy.
    // We don't need to eat all the hardware entropy for just shuffling, but
    // using it to initialize a PRNG is much better than relying on time.
    std::default_random_engine random(random_device());

	std::shuffle(deck.begin(), deck.end(), random);
}

int getCardValue(const Card& card) {
	int cardValue = 0;

	if (static_cast<int>(card.face) <= 8)
		cardValue = static_cast<int>(card.face) + 2;
	else if (static_cast<int>(card.face) < 12)
		cardValue = 10;
	else
		cardValue = 11;

	return cardValue;
		
}

int hit(Deck& deck, Hand& hand, int draw) {
	hand.push_back(deck[draw]);
    std::cout << "New Hand: ";
    printHand(hand);
    std::cout << '\n';
	return getCardValue(deck[draw]);
}

bool playBlackJack(Deck& deck) {
	int cardsDelt= 4;
	int	player_points{};
	int dealer_points{};
	int selection{};

	std::vector<Card> player_hand { deck[0], deck[2] };
	std::vector<Card> dealer_hand { deck[1], deck[3] };

	for (Card card : player_hand) {
		player_points += getCardValue(card);
	}

	for (Card card : dealer_hand) {
		dealer_points += getCardValue(card);
	}

	std::cout << "Your hand: " << '\n';
	printHand(player_hand);
	std::cout << '\n';
	std::cout << "The dealer's hand: " << '\n';
	printHand(dealer_hand);
	std::cout << '\n';

	std::cout << "Score:" << '\n';
	std::cout << "You: " << player_points << '\n';
	std::cout << "Dealer: " << dealer_points << '\n';

	std::cout << '\n';

	while (player_points < 21) {

		std::cout << "Would you like to hit or stand?" << '\n';
		std::cout << "1) Hit" << '\n';
		std::cout << "2) Stand" << '\n';
		std::cin >> selection;

		if (selection == 1) {	
			player_points += hit(deck, player_hand, cardsDelt);
			++cardsDelt;
			std::cout << "Your new score: " << player_points << '\n';
		}
		else
			break;
	}

	if (player_points > 21) {
		std::cout << "Score:" << '\n';
		std::cout << "You: " << player_points << '\n';
		std::cout << "Dealer: " << dealer_points << '\n';
		std::cout << "You bust! Better luck next time." << '\n';
		return false;
	}

	while (dealer_points < 17) {
		dealer_points += hit(deck, dealer_hand, cardsDelt);
		++cardsDelt;
		std::cout << "Dealer's new score: " << dealer_points << '\n';
	}

	if (dealer_points > 21) {
		std::cout << "Score:" << '\n';
		std::cout << "You: " << player_points << '\n';
		std::cout << "Dealer: " << dealer_points << '\n';
		std::cout << "The dealer busts! You win!" << '\n';
		return false;
	}

	std::cout << "Final scores: " << '\n';
	std::cout << "Player: " << player_points << '\n';
	std::cout << "Dealer: " << dealer_points << '\n';

	if (player_points > dealer_points) {
		std::cout << "You won!" << '\n';
		return true;
	}
	else {
		std::cout << "You lost. Better luck next time." << '\n';
		return false;
    }
}

int main() {

    bool play = true;

    while (play) {
        auto deck = createDeck();
        shuffleDeck(deck);
        playBlackJack(deck);

	if (selection == 1){
		auto newDeck = createDeck();
		shuffleDeck(newDeck);
		playBlackJack(newDeck);
	}
	else
		break;
        std::cout << "Would you like to play again?" << '\n';
        std::cout << "1) Yes" << '\n';
        std::cout << "2) No" << '\n';
        int selection{};
        std::cin >> selection;
        play = selection == 1;
    }

	return 0;
}

