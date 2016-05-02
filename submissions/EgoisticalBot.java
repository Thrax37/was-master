import java.util.ArrayList;
import java.util.List;

public class EgoisticalBot {

	int round;
	int playerID;
	int coins;
	
	List<Player> players;

    public static void main(String[] args){
        new EgoisticalBot().play(args[0].split(";"));
    }
    
    private void play(String[] args) {
    	
    	round = Integer.parseInt(args[0]);
    	playerID = Integer.parseInt(args[1]);
    	coins = Integer.parseInt(args[2]);
    	
    	players = new ArrayList<>();
		
        for (int i = 3; i < args.length; i++){
        	players.add(new Player(args[i]));
        }

        System.out.println("2FF");
    }
    
    private class Player {
		
    	private int ownerId;
        private int points;
        private int flippedCoins;
        private int unflippedCoins;
        
        public Player(String string) {
            String[] args = string.split("_");
            ownerId = Integer.parseInt(args[0]);
            points = Integer.parseInt(args[1]);
            flippedCoins = Integer.parseInt(args[2]);
            unflippedCoins = Integer.parseInt(args[3]);
        }
        
        public int getOwnerId() {
			return ownerId;
		}

		public int getPoints() {
			return points;
		}

		public void setPoints(int points) {
			this.points = points;
		}

		public int getFlippedCoins() {
			return flippedCoins;
		}

		public void setFlippedCoins(int flippedCoins) {
			this.flippedCoins = flippedCoins;
		}

		public int getUnflippedCoins() {
			return unflippedCoins;
		}

		public void setUnflippedCoins(int unflippedCoins) {
			this.unflippedCoins = unflippedCoins;
		}

		public void setOwnerId(int ownerId) {
			this.ownerId = ownerId;
		}

    }

}
