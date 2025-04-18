
package wordDictionary;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.io.*;
import java.util.*;

public class WordDictionary extends JFrame {
    private HashMap<String, String> dictionary;  // 단어와 뜻을 저장하는 HashMap
    private JTextField wordField;  // 단어 입력 필드
    private JTextArea meaningArea;  // 뜻 출력 영역

    public WordDictionary() {
        dictionary = new HashMap<>();  // HashMap 객체 생성

        // 창 설정
        setTitle("단어 뜻 검색 프로그램");
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // 단어 입력 필드
        JPanel inputPanel = new JPanel();
        JLabel wordLabel = new JLabel("단어:");
        wordField = new JTextField(15);
        JButton searchButton = new JButton("검색");
        inputPanel.add(wordLabel);
        inputPanel.add(wordField);
        inputPanel.add(searchButton);
        add(inputPanel, BorderLayout.NORTH);

        // 뜻 출력 영역
        meaningArea = new JTextArea();
        meaningArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(meaningArea);
        add(scrollPane, BorderLayout.CENTER);

        // 검색 버튼 클릭 이벤트 처리
        searchButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String word = wordField.getText();
                String meaning = dictionary.getOrDefault(word, "단어를 찾을 수 없습니다.");
                meaningArea.setText(word + ": " + meaning);
            }
        });

        // 삭제 버튼 클릭 이벤트 처리
        JButton deleteButton = new JButton("삭제");
        deleteButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String word = wordField.getText();
                if (dictionary.containsKey(word)) {
                    dictionary.remove(word);
                    meaningArea.setText("단어가 삭제되었습니다.");
                } else {
                    meaningArea.setText("단어를 찾을 수 없습니다.");
                }
            }
        });

        // 삽입 버튼 클릭 이벤트 처리
        JButton insertButton = new JButton("삽입");
        insertButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String word = wordField.getText();
                String meaning = JOptionPane.showInputDialog("뜻을 입력하세요:");

                if (meaning != null && !meaning.trim().isEmpty()) {
                    dictionary.put(word, meaning);
                    meaningArea.setText("단어가 추가되었습니다.");
                } else {
                    meaningArea.setText("단어 추가가 취소되었습니다.");
                }
            }
        });

        // 종료 버튼 클릭 이벤트 처리
        JButton exitButton = new JButton("종료");
        exitButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                saveDictionaryToFile();
                System.exit(0);
            }
        });

        // 버튼 패널
        JPanel buttonPanel = new JPanel();
        buttonPanel.add(deleteButton);
        buttonPanel.add(insertButton);
        buttonPanel.add(exitButton);
        add(buttonPanel, BorderLayout.SOUTH);

        // 파일에서 단어장 읽어오기
        loadDictionaryFromFile();
    }

    // "dictionary.txt" 파일에서 단어장을 읽어와 HashMap에 저장하는 메서드
    public void loadDictionaryFromFile() {
        try (BufferedReader reader = new BufferedReader(new FileReader("dictionary.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(":");
                if (parts.length == 2) {
                    String word = parts[0].trim();
                    String meaning = parts[1].trim();
                    dictionary.put(word, meaning);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // 단어장을 "dictionary.txt" 파일에 저장하는 메서드
    public void saveDictionaryToFile() {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("dictionary.txt"))) {
            for (Map.Entry<String, String> entry : dictionary.entrySet()) {
                writer.write(entry.getKey() + ": " + entry.getValue());
                writer.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
            	WordDictionary wordDictionary = new WordDictionary();
                wordDictionary.setVisible(true);
            }
        });
    }
}
