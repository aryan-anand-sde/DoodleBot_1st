const int ML1 = 5;
const int ML2 = 6;
const int MR1 = 9 ;
const int MR2 = 10 ;

const int Led = 13;

// Range (for v) : 0 to 255
int v = 75;
int vl = 100;
int vr = 93;

int ttl = 1100;
int ttr = 1300;
int st = 2000;

int i = 0;
char path[] = {'S', 'R', 'L', 'R', 'R', 'L', 'R', 'F'};

void setup() {
  // put your setup code here, to run once:
  pinMode(ML1, OUTPUT);
  pinMode(ML2, OUTPUT);
  pinMode(MR1, OUTPUT);
  pinMode(MR2, OUTPUT);
  pinMode(Led, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (i < sizeof(path)) {
    if (path[i] == 'S') {
      analogWrite(ML1, vl);
      analogWrite(ML2, 0);
      analogWrite(MR1, vr);
      analogWrite(MR2, 0);
      delay(st);
    }
    else if (path[i] == 'R') {
      analogWrite(ML1, v);
      analogWrite(ML2, 0);
      analogWrite(MR1, 0);
      analogWrite(MR2, 0);
      delay(ttr);
      analogWrite(ML1, vl);
      analogWrite(ML2, 0);
      analogWrite(MR1, vr);
      analogWrite(MR2, 0);
      delay(st);
    } else if (path[i] == 'L') {
      analogWrite(ML1, 0);
      analogWrite(ML2, 0);
      analogWrite(MR1, v);
      analogWrite(MR2, 0);
      delay(ttl);
      analogWrite(ML1, vl);
      analogWrite(ML2, 0);
      analogWrite(MR1, vr);
      analogWrite(MR2, 0);
      delay(st);
    } else {
      analogWrite(ML1, 0);
      analogWrite(ML2, 0);
      analogWrite(MR1, 0);
      analogWrite(MR2, 0);
    }
  } else {
    analogWrite(ML1, 0);
    analogWrite(ML2, 0);
    analogWrite(MR1, 0);
    analogWrite(MR2, 0);
    analogWrite(Led, v);
    digitalWrite(Led, HIGH);
    delay(2500);
    digitalWrite(Led, LOW);
  }
  i++;
}
