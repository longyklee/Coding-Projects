#include <bits/stdc++.h>
#include <termios.h>
#include <unistd.h>
#include <stdio.h>
using namespace std;
int getch(void)
{
    struct termios oldattr, newattr;
    int ch;
    tcgetattr(STDIN_FILENO, &oldattr);
    newattr = oldattr;
    newattr.c_lflag &= ~(ICANON | ECHO);
    tcsetattr(STDIN_FILENO, TCSANOW, &newattr);
    ch = getchar();
    tcsetattr(STDIN_FILENO, TCSANOW, &oldattr);
    return ch;
}
int getche(void)
{
    struct termios oldattr, newattr;
    int ch;
    tcgetattr(STDIN_FILENO, &oldattr);
    newattr = oldattr;
    newattr.c_lflag &= ~(ICANON);
    tcsetattr(STDIN_FILENO, TCSANOW, &newattr);
    ch = getchar();
    tcsetattr(STDIN_FILENO, TCSANOW, &oldattr);
    return ch;
}
int convert(char a)
{
    if (a == '1')
    {
        return 0;
    }
    if (a == '2')
    {
        return 1;
    }
    if (a == '3')
    {
        return 2;
    }
    if (a == '4')
    {
        return 3;
    }
    if (a == '5')
    {
        return 4;
    }
    if (a == 'q')
    {
        return 5;
    }
    if (a == 'w')
    {
        return 6;
    }
    if (a == '0')
    {
        return 7;
    }
    if (a == '9')
    {
        return 8;
    }
    if (a == '8')
    {
        return 9;
    }
    if (a == 'o')
    {
        return 10;
    }
    if (a == 'p')
    {
        return 11;
    }
    if (a == '=')
    {
        return 12;
    }
    return 99;
}

int main()
{
    cout << fixed << setprecision(2);
    string list[] = {
        "|  CHEESEBURGER  |   3.00  |   1  |", // 0
        "|    HAMBURGER   |   2.50  |   2  |", // 1
        "| PACKAGE (FRIES)|   1.50  |   3  |", // 2
        "| FOUNTAIN SODA  |   1.50  |   4  |", // 3
        "|     FRIES      |   1.00  |   5  |", // 4
        "|   COKEa-COLA   |   ----  |   q  |", // 5
        "|     SPRITE     |   ----  |   w  |", // 6
        "|   NO LETTUCE   |   ----  |   0  |", // 7
        "|    NO TOMATO   |   ----  |   9  |", // 8
        "| GRILLED ONION  |   ----  |   8  |", // 9
        "|         DISCOUNT         |   o  |"  // 10
        //"|          DELETE          |   p  |"  // 11
    };
    string item[] = {
        "|  CHEESEBURGER  |   3.00  |   1  |", // 0
        "|    HAMBURGER   |   2.50  |   2  |", // 1
        "- PACKAGE (FRIES)|   1.50  |   3  |", // 2
        "| FOUNTAIN SODA  |   1.50  |   4  |", // 3
        "|     FRIES      |   1.00  |   5  |", // 4
        "-   COKEa-COLA   |   ----  |   q  |", // 5
        "-     SPRITE     |   ----  |   w  |", // 6
        "-   NO LETTUCE   |   ----  |   0  |", // 7
        "-    NO TOMATO   |   ----  |   9  |", // 8
        "- GRILLED ONION  |   ----  |   8  |", // 9
        "|         DISCOUNT         |   o  |"  // 10
        //"|          DELETE          |   p  |"  // 11
    };
    double price[] = {3, 2.5, 1.5, 1.5, 1, 0, 0, 0, 0, 0};
    cout << "SINGLE-KEY POS SYSTEM" << endl;
    cout << "---------------MENU----------------" << endl;
    cout << "|      ITEM      |  PRICE  | CODE |" << endl;
    for (int i = 0; i < 10; i++)
    {
        cout << list[i] << endl;
    }
    cout << "-----------------------------------" << endl;
    cout << "|          OPTION          | CODE |" << endl;
    cout << list[10] << endl;
    cout << "|          DELETE          |   p  |" << endl;
    cout << "-----------------------------------" << endl;

    while (true)
    {
        cout << "\n-----------------NEW ORDER----------------" << endl;
        cout << "|      ITEM      |  PRICE  | CODE | TOTAL|";
        double total = 0.0;
        vector<int> totalSymbol;
        while (true)
        {
            char i = getch();
            int a = convert(i);
            if (a == 12) // 結單
            {
                cout << "\n|              TOTAL              | " << total << " |" << endl;
                cout << "Payment Method: 1. Credit Card\t 2. Debit Card\t3. Cash\t4. Loyalty Card (IN PROGRESS)\n";
                char pm = getch();
                if (pm == '1' || pm == '2')
                {
                    cout << "Please SWIPE your card.\n";
                    sleep(1);
                    cout << ".\n";
                    sleep(1);
                    cout << ".\n";
                    sleep(1);
                    cout << "Paid $" << total << endl;
                    cout << "Payment Success! Have a Great Day!";
                    break;
                }
                else
                {
                    double paid;
                    cout << "Amount Given: ";
                    cin >> paid;
                    if (paid < total)
                    {
                        cout << "Payment Failed. Try again later.";
                        break;
                    }
                    else
                    {
                        cout << "Payment Success!" << endl;
                        cout << "Change: $" << paid - total;
                        break;
                    }
                }
            }
            else if (a != 99) // NOT OUT OF RANGE
            {
                if (a == 11) // DELETE
                {
                    cout << "  ----DELETED----";
                    total -= price[totalSymbol.back()];
                    totalSymbol.pop_back();
                }
                else
                {
                    totalSymbol.push_back(a);
                    cout << endl;
                    double p;
                    cout << item[a];
                    if (a == 10) // DISCOUNT
                    {
                        cout << " ";
                        cin >> p;
                        cout << "\t** -$" << p << " **";
                        total -= p;
                    }
                    else
                    {
                        p = price[a];
                        total += p;
                        cout << " " << total << " |";
                    }
                }
            }
        }
        cout << "\n-----------------ORDER END----------------"
             << "\n\n";
    }
    return 0;
}