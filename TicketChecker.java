//Author Vincent Kwofie
//Date 24th May 2019
//Time 7:00PM

//Test using the following;
//123454 = true
//147103 = true
//154123 = false
import java.util.*;

public class TicketChecker
{
	public static void main(String[] args)
	{
		System.out.println("Hello Customer");
        
		//Read User Input
		Scanner input = new Scanner(System.in);
		System.out.println("Enter your ticket number for verification:");
		String number1 = input.next();
		
		//First five numbers and last number 
		String firstFive = number1.substring(0,5);
		String lastNumber = number1.substring(5);
		
		//Inter.parseInt() converts Strings to Integers
		int substring1 = Integer.parseInt(firstFive); 
		int substring2 = Integer.parseInt(lastNumber);
		
		//calculation and boolean checker
		int answer = substring1%7;
		boolean isTrue = (answer==substring2);
		System.out.printf("The first five numbers are %s%nLast number is %s%nThe ticket number is %s",firstFive,lastNumber,isTrue);
		
	}
}
