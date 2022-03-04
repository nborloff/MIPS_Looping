.data # necessary data
    one: .asciiz "One "
    two: .asciiz "Two "
    three: .asciiz "Three "
    four: .asciiz "Four "
    five: .asciiz "Five "
    six: .asciiz "Six "
    seven: .asciiz "Seven "
    eight: .asciiz "Eight "
    nine: .asciiz "Nine "
    zero: .asciiz "Zero "
    message_1: .asciiz "Please enter a positive integer: "
    message_2: .asciiz "Invalid Entry"
    user_input: .space 20 # hold input from user (how big should this be?)
    
.text
    main:
    	# Displays message_1
	li $v0, 4
	la $a0, message_1
	syscall    
    	
    	# getting user's input as text
    	li $v0, 8 # tell system to prepare for user input
    	la $a0, user_input # gonna pass user input to $a0
    	li $a1, 5 
    	syscall
       
    	# Displays the name
    	li $v0, 4
    	la $a0, user_input
    	syscall
    	
    # Tell the system this is the end of main
    li $v0, 10
    syscall