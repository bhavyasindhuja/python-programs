class Node{
    int data;
    Node nextNode;
    public Node(int data,Node nextNode){
        this.data=data;
        this.nextNode=nextNode;
    }
}
class Node{
    int data;
    Node prevNode;
    Node nextNode;
    public Node(int data,Node prevNode,Node nextNode){
        this.data=data;
        this.prevNode=prevNode;
        this.nextNode=nextNode;
    }
}

public class linkedList{
    public static void main(String[] args){
        Node n=new Node(5,null,null);
        Node n2=new Node(6,n,null);
        Node n3=new Node(7,n2,null);
        System.out.println("the value is:"+n.data);
    }
}