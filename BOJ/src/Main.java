import java.io.*;
import java.util.*;

class Data {
    String name;
    int korean;
    int english;
    int math;
    public Data(String name, int korean, int english, int math) {
        this.name = name;
        this.korean = korean;
        this.english = english;
        this.math = math;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));    
        int count = Integer.parseInt(in.readLine());
        ArrayList<Data> arrayList = new ArrayList<>();
        for(int i=0; i<count; ++i) {
            String[] input = in.readLine().split(" ");
            arrayList.add(new Data(input[0], Integer.parseInt(input[1]), Integer.parseInt(input[2]), Integer.parseInt(input[3])));
        }
        Collections.sort(arrayList, new Comparator<Data>() {
        	@Override
			public int compare(Data a, Data b) {
				if (a.korean > b.korean) {
					return -1;
				} else if (a.korean == b.korean) {
					if (a.english == b.english) {
						if (a.math == b.math) {
							return a.name.compareTo(b.name);
						}
						return Integer.compare(Integer.valueOf(b.math), Integer.valueOf(a.math));
					}
					return Integer.compare(Integer.valueOf(a.english), Integer.valueOf(b.english));
				} else {
					return 1;
				}
			}
        });
        for(int i=0; i<count; ++i) {
            System.out.println(arrayList.get(i).name);
        }
    }
}