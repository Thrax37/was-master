package controller;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import players.Balance;
import players.BirdInTheHand;
import players.Crook;
import players.EgoisticalBot;
import players.Flipper;
import players.GreedyRotation;
import players.Jim;
import players.Oracle;
import players.PassiveBot;
import players.Saboteur;
import players.SimpleBot;
import players.TheJanitor;

public class Game {
	private static Player[] players = {
		new Balance(),
		new BirdInTheHand(),
		new Crook(),
		new EgoisticalBot(),
		new Flipper(),
		new GreedyRotation(),
		new Jim(),
		new Oracle(),
		new PassiveBot(),
		new Saboteur(),
		new SimpleBot(),
		new TheJanitor()
	};
	
	// Game Parameters
	private static int COINS;
	private static final int GAMES = 20;
	private static final int ROUNDS = 50;
	private static final int NB_ACTIONS = 3;
	
	private static final int POINTS_TAKE = -1;
	private static final int POINTS_PUT = 1;
	private static final int POINTS_REMOVE = 0;
	private static final int POINTS_FLIP = 2;
	private static final int POINTS_UNFLIP = -2;
	private static final int POINTS_GET_FLIPPED = 2;
	private static final int POINTS_GET_UNFLIPPED = -1;
	private static final int POINTS_END_FLIPPED = 2;
	private static final int POINTS_END_UNFLIPPED = -1;
	
	// Console
	private static final boolean DEBUG = false;
	private static final boolean GAME_MESSAGES = false;
		
	private final List<PlayerType> playerTypes = new ArrayList<PlayerType>();
	private int round = 0;
	
	public Game() {
		for (int i = 0; i < players.length; i++) {
			players[i].setId(i);
		}
		
		int x = players.length;
		int r = (int) (Math.random() * Math.pow(x, 2) + 1);
		
		Game.COINS = (int) (Math.pow(2, x) + (x * 10) - r);
	}
	
	public static void main(String... args) {
		
		List<List<Score>> totalScores = new ArrayList<>();
		
		// Starting
		for (int i = 0; i < GAMES; i++) {
			totalScores.add(new Game().run());
		}
		
		// Scores
		Map<Player, List<Score>> playerScores = new HashMap<>();
		List<Score> finalScores = new ArrayList<>();
		for (List<Score> scores : totalScores) {
			for (Score score : scores) {
				if (playerScores.get(score.getPlayer()) == null) {
					playerScores.put(score.getPlayer(), new ArrayList<>());
				}
				playerScores.get(score.getPlayer()).add(score);
			}
		}
		for (Player player : playerScores.keySet()) {
			int points = 0;
			for (Score score : playerScores.get(player)) {
				points += score.getPoints();
			}
			finalScores.add(new Score(player, points));
		}
		
		//sort descending
		Collections.sort(finalScores, Collections.reverseOrder());
		
		System.out.println("################################");
		for (int i = 0; i < finalScores.size(); i++) {
			Score score = finalScores.get(i);
			System.out.println(i+1 + ". " + score.print());
		}
	}	
	
	public List<Score> run() {
			
		if (GAME_MESSAGES) 
			System.out.println("Starting a new game...");
		
		this.initialize();
		
		if (GAME_MESSAGES) 
			System.out.println("Game begins.");
							
		for (round = 1; round <= ROUNDS; round++) {
			if (GAME_MESSAGES) {
				System.out.println("-- Round : " +  round + " -- (" + Game.COINS + " coins left)");
			}
			if (!makeTurns()) break; //break if only no player left or monster dead
		}
		
		countCoins();
	
		return printResults();
	}

	private void initialize() {
		
		for (int i = 0; i < players.length; i++) {
			try {
				if (GAME_MESSAGES) System.out.println("Player \"" + players[i].getDisplayName() + "\" added.");
				PlayerType playerType = new PlayerType(i, players[i], 0, 0, 0);
				playerTypes.add(playerType);
			} catch (Exception e) {
				if (DEBUG) {
					System.out.println("Exception in initialize() by " + players[i].getDisplayName());
					e.printStackTrace();
				}
			}
		}
		
		Collections.shuffle(playerTypes);
		for (int i = 0; i < playerTypes.size(); i++) {
			playerTypes.get(i).setOrder(i);
		}
	}	
	
	private boolean makeTurns() {
		
		Collections.sort(playerTypes);
		
		for (PlayerType playerType : playerTypes) {
					
			Player owner = playerType.getOwner();
			try {
				String request = round + ";" + owner.getId() + ";" + Game.COINS + generateArgs();
				String response = playerType.getCommand(request);
				if (DEBUG) {
					System.out.println("Request : " + request);
					System.out.println("Response : " + response);
				}
				if (response.length() < NB_ACTIONS) {
					throw new Exception("Invalid response length : " + response.length());
				}
				
				for (int i = 0; i < NB_ACTIONS; i++) {
					switch (response.charAt(i)) {
						case '1': executeTake(playerType, 1); break;
						case '2': executeTake(playerType, 2); break;
						case '3': executeTake(playerType, 3); break;
						case 'A': executePut(playerType, 1); break;
						case 'B': executePut(playerType, 2); break;
						case 'C': executePut(playerType, 3); break;
						case 'R': executeRotate(playerType, 0); break;
						case 'T': executeRotate(playerType, 1); break;
						case 'F': executeFlip(playerType); break;
						case 'U': executeUnflip(playerType); break;
						case 'X': executeRemove(playerType, 1); break;
						case 'Y': executeRemove(playerType, 2); break;
						case 'Z': executeRemove(playerType, 3); break;
						case 'N': executeWait(playerType); break;
						default : executeWait(playerType); break;
					}
				}
					
			} catch (Exception e) {
				if (DEBUG) {
					System.out.println("Exception in makeTurns() by " + owner.getDisplayName());
					e.printStackTrace();
				}
			}
					
			if (gameOver())
				return false;
		}
		
		return true;
	}
	
	private boolean gameOver() {
		return COINS <= 0;
	}
	
	private void executeTake(PlayerType player, int nb) {
		
		int maxCoins = Game.COINS >= nb ? nb : Game.COINS;
		
		Game.COINS -= maxCoins;
		player.setUnflippedCoins(player.getUnflippedCoins() + maxCoins);
		player.setPoints(player.getPoints() + (maxCoins * POINTS_TAKE));
		
		if (GAME_MESSAGES) System.out.println(player.getOwner().getDisplayName() + " took " + maxCoins + " coins. (" + Game.COINS + " coins left)." + displayStats(player));
	}
	
	private void executePut(PlayerType player, int nb) {
		
		int maxCoins = player.getUnflippedCoins() >= nb ? nb : player.getUnflippedCoins() ;
		
		Game.COINS += maxCoins;
		player.setUnflippedCoins(player.getUnflippedCoins() - maxCoins);
		player.setPoints(player.getPoints() + (maxCoins * POINTS_PUT));
		
		if (GAME_MESSAGES) System.out.println(player.getOwner().getDisplayName() + " put back " + maxCoins + " coins. (" + Game.COINS + " coins left)." + displayStats(player));
	}
	
	private void executeRotate(PlayerType player, int direction) {
		
		PlayerType tempPlayer = new PlayerType(0, null, 0, 0, 0);
		int unflippedCoins = 0;
		int flippedCoins = 0;
		
		if (direction == 0) { // To previous
			
			tempPlayer.setUnflippedCoins(playerTypes.get(0).getUnflippedCoins());
			tempPlayer.setFlippedCoins(playerTypes.get(0).getFlippedCoins());
			
			for (int i = 0; i < playerTypes.size(); i++) {
				if (i + 1 > playerTypes.size() - 1) {
					unflippedCoins = tempPlayer.getUnflippedCoins();
					flippedCoins = tempPlayer.getFlippedCoins();
				} else {
					unflippedCoins = playerTypes.get(i + 1).getUnflippedCoins();
					flippedCoins = playerTypes.get(i + 1).getFlippedCoins();
				}
				playerTypes.get(i).setUnflippedCoins(unflippedCoins);
				playerTypes.get(i).setFlippedCoins(flippedCoins);
				playerTypes.get(i).setPoints(playerTypes.get(i).getPoints() + (unflippedCoins * POINTS_GET_UNFLIPPED) + (flippedCoins * POINTS_GET_FLIPPED));
			}
			
			if (GAME_MESSAGES) System.out.println(player.getOwner().getDisplayName() + " rotated coins to previous player." + displayStats(player));
			
		} else if (direction == 1) { // To next
			
			tempPlayer.setUnflippedCoins(playerTypes.get(playerTypes.size() - 1).getUnflippedCoins());
			tempPlayer.setFlippedCoins(playerTypes.get(playerTypes.size() - 1).getFlippedCoins());
		
			for (int i = playerTypes.size() - 1; i >= 0 ; i--) {
				if (i < 1) {
					unflippedCoins = tempPlayer.getUnflippedCoins();
					flippedCoins = tempPlayer.getFlippedCoins();
				} else {
					unflippedCoins = playerTypes.get(i - 1).getUnflippedCoins();
					flippedCoins = playerTypes.get(i - 1).getFlippedCoins();
				}
				playerTypes.get(i).setUnflippedCoins(unflippedCoins);
				playerTypes.get(i).setFlippedCoins(flippedCoins);
				playerTypes.get(i).setPoints(playerTypes.get(i).getPoints() + (unflippedCoins * POINTS_GET_UNFLIPPED) + (flippedCoins * POINTS_GET_FLIPPED));
			}
			
			if (GAME_MESSAGES) System.out.println(player.getOwner().getDisplayName() + " rotated coins to next player." + displayStats(player));
			
		}
	}

	
	private void executeRemove(PlayerType player, int nb) {
		
		int maxCoins = player.getUnflippedCoins() >= nb ? nb : player.getUnflippedCoins() ;
		
		player.setUnflippedCoins(player.getUnflippedCoins() - maxCoins);
		player.setPoints(player.getPoints() + (maxCoins * POINTS_REMOVE));
		
		if (GAME_MESSAGES) System.out.println(player.getOwner().getDisplayName() + " removed " + maxCoins + " coins from the pot. (" + Game.COINS + " coins left)." + displayStats(player));		
	}
		
	private void executeFlip(PlayerType player) {
		
		int maxCoins = player.getUnflippedCoins() >= 1 ? 1 : player.getUnflippedCoins() ;
		
		player.setUnflippedCoins(player.getUnflippedCoins() - maxCoins);
		player.setFlippedCoins(player.getFlippedCoins() + maxCoins);
		player.setPoints(player.getPoints() + (maxCoins * POINTS_FLIP));
		
		if (GAME_MESSAGES) System.out.println(player.getOwner().getDisplayName() + " flipped " + maxCoins + " coin." + displayStats(player));
	}
	
	private void executeUnflip(PlayerType player) {
		
		int maxCoins = player.getFlippedCoins() >= 1 ? 1 : player.getFlippedCoins() ;
		
		player.setUnflippedCoins(player.getUnflippedCoins() + maxCoins);
		player.setFlippedCoins(player.getFlippedCoins() - maxCoins);
		player.setPoints(player.getPoints() + (maxCoins * POINTS_UNFLIP));
		
		if (GAME_MESSAGES) System.out.println(player.getOwner().getDisplayName() + " unflipped " + maxCoins + " coin." + displayStats(player));
	}
	
	private void executeWait(PlayerType player) {}
	
	private String generateArgs() {
		
		StringBuilder builder = new StringBuilder();
		//PlayerID_Score_Flipped_Unflipped
		for (PlayerType playerType : playerTypes) {
			builder.append(';');
			builder.append(playerType.getOwner().getId()).append('_');
			builder.append(playerType.getPoints()).append('_');
			builder.append(playerType.getFlippedCoins()).append('_');
			builder.append(playerType.getUnflippedCoins());
		}
		return builder.toString();
	}
	
	private void countCoins() {
		for (PlayerType player : playerTypes) {
			player.setPoints(player.getPoints() + (player.getFlippedCoins() * POINTS_END_FLIPPED) + (player.getUnflippedCoins() * POINTS_END_UNFLIPPED));
			
			if (GAME_MESSAGES) System.out.println(player.getOwner().getDisplayName() + " got " + ((player.getFlippedCoins() * POINTS_END_FLIPPED) + (player.getUnflippedCoins() * POINTS_END_UNFLIPPED)) + " points for his coins. (" + player.getUnflippedCoins() + " unflipped / " + player.getFlippedCoins() + " flipped)." + displayStats(player));
		}
	}

	private String displayStats(PlayerType player) {
		 return " [" + player.getPoints() + ", " + player.getUnflippedCoins() + ", " + player.getFlippedCoins() + "]";
	}
	
	private List<Score> printResults() {
		
		List<Score> scores = new ArrayList<Score>();
		
		System.out.println("********** FINISH **********");
		
		for (Player player : players) {
			int points = 0;
			
			for (PlayerType playerType : playerTypes) {
				if (player.equals(playerType.getOwner())) {
					points += playerType.getPoints();
					
				}
			}
			
			scores.add(new Score(player, points));
		}
		
		//sort descending
		Collections.sort(scores, Collections.reverseOrder());
		
		for (int i = 0; i < scores.size(); i++) {
			Score score = scores.get(i);
			System.out.println(i+1 + ". " + score.print());
		}
		
		return scores;
	}
	
}

