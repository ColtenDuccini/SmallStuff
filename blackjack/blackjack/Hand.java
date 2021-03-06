package blackjack;
import java.util.*;

public class Hand {
    private ArrayList<Card> cards;

    public Hand(){
	cards = new ArrayList<Card>();
    }
    
    public void addCard(Card c){
	cards.add(c);
    }

    public ArrayList<Card> clearHand(){
	ArrayList<Card> discards = new ArrayList<Card>(cards);
	cards.clear();
	return discards;
    }
    
    @Override
    public String toString(){
	String output = "";
	for (Card c : cards){
	    output = output.concat(c.toString() + "; ");
	}
	if (isBlackjack()){
	    output = output.concat("value = " + 21);
	}
	else {
	    output = output.concat("value = " + getValue());
	}
	return output;
    }
    public String showFirstCard(){
	return cards.get(0).toString();
    }

    public int getValue(){
	int total = 0;
	for (Card c : cards){
	    int cardValue = c.getValue();
	    if (cardValue == 1)  // Rules for handling aces
		{
		if (total + 11 < 21) // If counting the ace as an 11 won't lead to a bust,
		    { 
		    total += 11; // then count it as an 11;
		    }
		else // otherwise,
		    {
			total += 1; // count it as a one.
		    }
		}
	    else
		{
		    total += cardValue;
		}
	}
	return total;
    }

    public boolean isBust(){
	return (getValue() > 21);
    }
    
    public boolean isBlackjack() 
    {
	/* For a hand to be a blackjack, it must contain only 2 cards,
	   an ace and a face card. */
        if (cards.size() == 2) 
	    {
	    Card c1 = cards.get(0);
	    Card c2 = cards.get(1);
	    if (c1.getValue() == 1)
		{
		return (c2.getValue() == 10);
		}
	    else if (c2.getValue() == 1) 
		{
		    return (c1.getValue() == 10);
		}
	    else return false;
	    }
	return false;
    }
}
