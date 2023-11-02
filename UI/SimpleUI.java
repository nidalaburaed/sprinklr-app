import javax.swing.*;

public class SimpleUI {
    public static void main(String[] args) {
        // Create a JFrame (the main window)
        JFrame frame = new JFrame("Simple Java UI Example");
        
        // Create a button
        JButton button = new JButton("Click Me");
        
        // Add the button to the frame
        frame.add(button);
        
        // Set frame properties
        frame.setSize(300, 200); // Set size
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Close operation
        frame.setVisible(true); // Make the frame visible
    }
}