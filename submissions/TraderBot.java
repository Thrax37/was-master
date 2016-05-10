import java.util.ArrayList;
import java.util.List;

public class TraderBot {

class Player{
    private int id;
    private int points;
    private int flip;
    private int unflip;

    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public int getPoints() {
        return points;
    }
    public void setPoints(int points) {
        this.points = points;
    }
    public int getFlip() {
        return flip;
    }
    public void setFlip(int flip) {
        this.flip = flip;
    }
    public int getUnflip() {
        return unflip;
    }
    public void setUnflip(int unflip) {
        this.unflip = unflip;
    }


}

int round;
int coins;
int otherMaxPoints = 0;
Player myself = new Player();
List<Player> players = new ArrayList<>();

public static void main (String[] s){
    new TraderBot().play(s);
}

private void play(String[] s){
    parse(s[0]);
    System.out.println(action() + action() + action());
}

private int simRotateNext(){
    int flip, unflip;
    int maxP = Integer.MIN_VALUE;
    Integer[] points = new Integer[players.size()];
    for (int i = 0; i < players.size(); i++){
        flip = players.get(i).getFlip();
        unflip = players.get(i).getUnflip();
        int next = i + 1 <= players.size() - 1 ? i + 1 : 0;
        int p = 2 * flip - unflip;
        if (p > maxP && players.get(next).getId() != myself.getId()){
            maxP = p;
        }
        points[next] = p;

    }
    return  points[myself.getId()] - maxP;
}

private int simRotatePrev(){
    int flip, unflip;
    int maxP = Integer.MIN_VALUE;
    Integer[] points = new Integer[players.size()];
    for (int i = players.size() -1; i >= 0; i--){
        flip = players.get(i).getFlip();
        unflip = players.get(i).getUnflip();
        int prev = i - 1 >= 0 ? i - 1 : players.size() - 1;
        int p = 2 * flip - unflip;
        if (p > maxP && players.get(prev).getId() != myself.getId()){
            maxP = p;
        }
        points[prev] = p;

    }
    return  points[myself.getId()] - maxP;
}

private void rotateNext(){
    int flip, unflip;
    for (int i = 0; i < players.size(); i++){
        flip = players.get(i).getFlip();
        unflip = players.get(i).getUnflip();
        int next = i + 1 <= players.size() - 1 ? i + 1 : 0;
        players.get(next).setFlip(flip);
        players.get(next).setUnflip(unflip);
        players.get(next).setPoints(players.get(next).getPoints() + 2 * flip - unflip);
    }
}

private void rotatePrev(){
    int flip, unflip;
    for (int i = players.size() -1; i > 0; i--){
        flip = players.get(i).getFlip();
        unflip = players.get(i).getUnflip();
        int prev = i - 1 >= 0 ? 0 : players.size() - 1;
        players.get(prev).setFlip(flip);
        players.get(prev).setUnflip(unflip);
        players.get(prev).setPoints(players.get(prev).getPoints() + 2 * flip - unflip);
    }
}

private String action() {
    int next = simRotateNext();
    int prev = simRotatePrev();

    if (next > 0 || prev > 0){
        if (next > prev){
            rotateNext();
            return "T";
        } else {
            rotatePrev();
            return "R";
        }
    }

    if (myself.getUnflip() > 3){
        myself.unflip -= 3;
        myself.points += 3;
        return "C";
    }

    if (myself.getUnflip() > 0){
        myself.unflip -= 1;
        myself.points += 2;
        return "F";
    }

    if (myself.getPoints() > otherMaxPoints){
        return "N";
    } else {
        myself.unflip += 3;
        myself.points -= 3;
        return "3";
    }

}

private void parse(String s){
    String[] ps = s.split(";");
    round = Integer.parseInt(ps[0]);
    myself.setId(Integer.parseInt(ps[1]));
    coins = round = Integer.parseInt(ps[2]);
    for (int i = 3; i < ps.length; i++){
        String[] sp2 = ps[i].split("_");
        if (sp2[0].equals(myself.getId())){
            myself.setPoints(Integer.parseInt(sp2[1]));
            myself.setFlip(Integer.parseInt(sp2[2]));
            myself.setUnflip(Integer.parseInt(sp2[3]));
            players.add(myself);
        } else {
            Player p = new Player();
            p.setId(Integer.parseInt(sp2[0]));
            p.setPoints(Integer.parseInt(sp2[1]));
            p.setFlip(Integer.parseInt(sp2[2]));
            p.setUnflip(Integer.parseInt(sp2[3]));
            players.add(p);
            if (p.getPoints() > otherMaxPoints){
                otherMaxPoints = p.getPoints();
            }
        }
    }
}

}