const int md1 = 6; // Pra começar o código nos definimos as váriaveis que nos utilizaremos! // PINO DO MOTOR DIREITO
const int md2 = 5; // 'md' significa Motor Direito e 'me' Motor Esquerdo!
const int me3 = 10;
const int me4 = 9; // PINO DO MOTOR ESQUERDO
const int sn_e = A3; // Aqui nos definimos os pinos dos sensores! 'sn_e' sendo o sensor esquerdo na visão traseira do carrinho!
const int sn_m = A1; // 'sn_m' sendo o sensor do meio do carrinho!
const int sn_d = A2; // 'sn_d' sendo o sensor da direita do carrinho na visão traseira!

const int velocidade = 80;

void setup() {
  pinMode(md1, OUTPUT); // Aqui nos declaramos os valores das portas!
  pinMode(md2, OUTPUT);
  pinMode(me3, OUTPUT); // Definimos os motores como SAIDA!
  pinMode(me4, OUTPUT);
  pinMode(sn_d, INPUT_PULLUP); // E os sensores como ENTRADA! (O PULLUP inverte a lógica do HIGH e do LOW no funcionamento dos sensores)
  pinMode(sn_m, INPUT_PULLUP);
  pinMode(sn_e, INPUT_PULLUP);

}

void loop() {
  
  if(digitalRead(sn_m) == LOW){ // Se o sensor do meio estiver ativo, o carrinho vai andar pra frente!
    digitalWrite(md1, velocidade);
    digitalWrite(md2, LOW);

    digitalWrite(me3, LOW);
    digitalWrite(me4, velocidade);
  }

  else if(digitalRead(sn_e) == LOW){ // Se o sensor da esquerda estiver ativo, o carrinho vai se acertar e seguir a rota!
    digitalWrite(md1, velocidade);
    digitalWrite(md2, LOW);

    digitalWrite(me3, LOW);
    digitalWrite(me4, 0);
  }

  else if (digitalRead(sn_d) == LOW){ // Se o sensor da direita estiver ativo, o carrinho vai se acertar e seguir a rota!
    digitalWrite(md1, 0);
    digitalWrite(md2, LOW);

    digitalWrite(me3, LOW);
    digitalWrite(me4, velocidade);
  }

  else {
    digitalWrite(md1, 0);
    digitalWrite(me4, 0);
  }
  
}
