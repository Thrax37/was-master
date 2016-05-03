package players;

import controller.Player;

public class Jim extends Player {

	@Override
	public String getCmd() {
		return "C:/ruby193/bin/ruby.exe Jim.rb";
	}	
}
