#include <fstream>
#include <iostream>
#include <string>
using namespace std;
#define nl system("echo ")

void print_error(int i, int t) {
    nl;
    string s = "echo \"Failed on case " + to_string(i) + "/" + to_string(t) + "\"";
    system(s.c_str());
    nl;
    system("echo Input data:");
    system("cat in");
    nl;
    system("echo Slow output:");
    system("cat slow.txt");
    nl;
    system("echo Fast output");
    system("cat fast.txt");
    nl;
    system("echo Difference");
    system("diff -c slow.txt fast.txt");
    cout.flush();
}

void remove_files() {
    system("rm -f gen");
    system("rm -f slow");
    system("rm -f fast");
    system("rm -f slow.txt");
    system("rm -f fast.txt");
    system("rm -f script");
    system("rm -f in");
}

int main(int argc, char *argv[]) {
    if (argc < 5) {
        return 1; 
    }
    string gen_file = argv[1]; // Generator file
    string slow_file = argv[2]; // Slow file
    string fast_file = argv[3]; // Fast file
    int t = atoi(argv[4]); // Number of cases
    int a = system(("g++ " + gen_file + " -o gen").c_str());
    int b = 0;
    // int b = system(("g++ " + slow_file + " -o slow").c_str());
    b = system(("python " + slow_file).c_str());
    return 0;
    int c = system(("g++ " + fast_file + " -o fast").c_str());

    if (a || b || c) { // If compilation error, break and delete files
        cout << "Compilation error\n";
        system("rm -f gen");
        system("rm -f slow");
        system("rm -f fast");
        return 1;
    }

    system("touch fast.txt");
    system("touch slow.txt");
    system("touch in");
    fstream fast;
    fstream slow;
    fast.open("fast.txt");
    slow.open("slow.txt");
    string f;
    string s;
    string str;
    int fc;
    int sc;
    for (int i = 1; i <= t; ++i) { // Run fast slow t times
        system("./gen > in");
        // system("./slow < in > slow.txt");
        system(("in > python " + slow_file).c_str());
        system("./fast < in > fast.txt");
        fc = 0;
        sc = 0;
        while (getline(fast, str)) ++fc; // Check that the files have the same number of lines
        while (getline(slow, str)) ++sc;
        if (fc != sc) {
            print_error(i, t);
            fast.close();
            slow.close();
            remove_files();
            return 1;
        }
        fast.clear();
        slow.clear();
        fast.seekg(0);
        slow.seekg(0);
        while (getline(fast, f) && getline(slow, s)) { // Compare each line 
            if (f != s) {
                print_error(i, t);
                fast.close();
                slow.close();
                remove_files();
                return 1;
            }
        }
        fast.clear();
        slow.clear();
        fast.seekg(0);
        slow.seekg(0);
    }
    fast.close();
    slow.close();
    cout << "Passed all cases!\n";
    remove_files();

    return 0;
}
