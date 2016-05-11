import java.util.ArrayList;
import java.util.List;

public class Wheeler {

String[] actions = {"TTT", "TTR", "TRR", "TRT", "RRR", "RRT", "RTR", "RTT"};
String paramString;

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
    @Override
    public String toString() {
        return "Player [id=" + id + ", points=" + points + ", flip=" + flip + ", unflip=" + unflip + "]";
    }




}

int round;
int coins;
int otherMaxPoints = 0;
Player myself = new Player();
List<Player> players = new ArrayList<>();

public static void main (String[] s){
    new Wheeler().play(s);
}

private void play(String[] s){
    paramString = s[0];
    reset();
    System.out.println(action());
}

private int rotateNext(){
    int flip, unflip, nflip, nunflip;
    flip = players.get(0).getFlip();
    unflip = players.get(0).getUnflip();
    for (int i = 0; i < players.size(); i++){
        int next = i + 1 <= players.size() - 1 ? i + 1 : 0;
        nflip = players.get(next).getFlip();
        nunflip = players.get(next).getUnflip();
        players.get(next).setFlip(flip);
        players.get(next).setUnflip(unflip);
        players.get(next).setPoints(players.get(next).getPoints() + 2 * flip - unflip);
        flip = nflip;
        unflip = nunflip;
    }
    return myself.getPoints();
}

private int rotatePrev(){
    int flip, unflip,  nflip, nunflip;
    flip = players.get(players.size() -1).getFlip();
    unflip = players.get(players.size() -1).getUnflip();
    for (int i = players.size() -1; i > 0; i--){
        int prev = i - 1 >= 0 ? i - 1 : players.size() - 1;
        nflip = players.get(prev).getFlip();
        nunflip = players.get(prev).getUnflip();
        players.get(prev).setFlip(flip);
        players.get(prev).setUnflip(unflip);
        players.get(prev).setPoints(players.get(prev).getPoints() + 2 * flip - unflip);
        flip = nflip;
        unflip = nunflip;
    }
    return myself.getPoints();
}

private String action() {
    int maxPoints = myself.getPoints();
    String action = "1F2";
    for (String s : actions){
        int cPoints = 0;
        for (char c : s.toCharArray()){
            if (c == 'T'){
                cPoints += rotateNext();
            } else {
                cPoints += rotatePrev();
            }
        }
        if (cPoints > maxPoints){
            action = s;
        }
        reset();
    }
    return action;      
}


private void reset(){
    players = new ArrayList<>();
    String[] ps = paramString.split(";");
    round = Integer.parseInt(ps[0]);
    myself.setId(Integer.parseInt(ps[1]));
    coins = round = Integer.parseInt(ps[2]);
    for (int i = 3; i < ps.length; i++){
        String[] sp2 = ps[i].split("_");
        if (Integer.parseInt(sp2[0]) == myself.getId()){
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