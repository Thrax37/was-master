package controller;


public class Score implements Comparable<Score> {
	private Player player;
	private int points;
	
	public Score(Player player, int points) {
		super();
		this.player = player;
		this.points = points;
	}
	
	public String print() {
		return player.getDisplayName() + ": " + points;
	}
	
	@Override
	public int compareTo(Score other) {
		if (points > other.points) {
			return 1;
		} else if (points < other.points){
			return -1;
		}

		return 0;
	}

	public Player getPlayer() {
		return player;
	}

	public void setPlayer(Player player) {
		this.player = player;
	}

	public int getPoints() {
		return points;
	}

	public void setPoints(int points) {
		this.points = points;
	}	
	
	
}
