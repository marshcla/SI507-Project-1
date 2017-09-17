Before cloning this code, users should have Python 3 installed on their computers.

The file SI507F17_project1_cards contains code for the project Cards, which simulates a version of the classic card game War.

It imports random and a file containing helper functions. The file helper_functions contains a function Song, which, at the game's conclusion, returns a song pulled from iTunes' API.

In the file SI507F17_project1_tests are test cases for the code. This file imports unittest in addition to the helper functions file.

Players initiate the game by invoking Class Card, which has three variables: suit_names (referring to 'Diamonds', 'Clubs', 'Hearts', and 'Spades'), rank_levels (1-13), and faces (a dictionary whose keys are 1, 11, 12, and 13, respectively, and whose values are Ace, Jack, Queen, and King).

Users input an integer representing suit (0-3) and rank (1-13). Card's default values are 0 and 2, respectively.

Class Deck represents the whole deck. It initializes a list of Card instances and appends them in a list.

It has five methods:
1. pop_card removes a single card from the deck
2. shuffle shuffles the remaining cards in the deck
3. replace_card takes as input a card instance and returns a card to the deck of it is not already there
4. sort_cards sorts the deck by suit
5. deal_hand takes as input an integer representing hand size and invokes pop_card as many times as the integer that was inputted.

Now players can actually play the game by invoking the function play_war_game. This initializes two instances of Class Deck and shuffles them. It then continues to invoke pop_card on each deck and compare the values. The player with the higher ranked card wins a point. This goes on until all the cards have been popped off.

The game has three results: Player1 wins OR Player2 wins OR Tie

At the end of the game, the show_song function (with default input being the string "Winner"--although it should handle any search term) invokes the helper function Song, which makes a call to the iTunes API and returns a song found using that search term.