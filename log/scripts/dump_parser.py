import json
import sys
from datetime import datetime

def mainloop():
	if len(sys.argv) < 2:
		print "enter json file"
		sys.exit(0)
	
	f = open(sys.argv[1]);
	players = json.loads(f.read());
	
	print "Number of players: %d" % len(players)
	
	for player in players:
		print ""
		print "Player %s" % player['uid']
		print "\tNumber of page loads (visits): %d" % len(player['pageloads'])
		print "\tNumber of levels played: %d" % len(player['levels'])
		
		levels = player['levels']
		for level in levels:
			print "\t\tLevel/'Quest' id: %s (%s)" % (level['qid'], datetime.fromtimestamp(level['log_q_ts']))
			print "\t\tLevel Start Event Detail %s" % level['q_detail']
			if level['quest_end'] is not None:
				print "\t\tLevel End Event Detail %s" % level['quest_end']['q_detail']
			
			actions = level['actions']
			for action in actions:
				print "\t\t\tAID: %s, Timestamp: %s, Action details: %s" % (action['aid'], action['ts'], action['a_detail'])
mainloop()
