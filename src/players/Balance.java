package players;

import controller.Player;

public class Balance extends Player {

	@Override
	public String getCmd() {
		return "C:/lua-5.3.2/bin/lua.exe Balance.lua";
	}	
}
