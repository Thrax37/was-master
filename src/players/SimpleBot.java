package players;

import controller.Player;

public class SimpleBot extends Player {

	@Override
	public String getCmd() {
		return "C:/python34/python3.exe SimpleBot.py";
	}	
}
