package players;

import controller.Player;

public class Crook extends Player {

	@Override
	public String getCmd() {
		return "C:/R-3.2.3/bin/Rscript.exe Crook.R";
	}	
}
