//Created by Vincent Kwofie.
//Date on the 24 May 2019.
//Time 8:43 PM

//Test using the following;
//123454 = true
//147103 = true
//154123 = false

import java.util.*;
public class TicketChecker2
{
	public static void main(String []args){
		System.out.println("Hello traveler!");
		
		//Read User Input
		Scanner input = new Scanner(System.in);
		System.out.println("Please enter your ticket number for verification: ");
		int ticketNumber = input.nextInt();
		
		//Trick for last number.
		int lastNumber = (ticketNumber-(ticketNumber/10)*10);
		
		//Trick for first four numbers.
		int firstFour = ticketNumber/10;
		
		//Boolean checker
		boolean isTrue = (firstFour%7==lastNumber);
		System.out.printf("First four numbers :%d%nLast number :%d%nThe ticket number is %b",firstFour,lastNumber,isTrue);
		
		
	}
}
