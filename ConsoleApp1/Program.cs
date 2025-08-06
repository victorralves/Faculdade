double N1 = ;
double N2 = ;

while (N1 > 0 && N1 <= 10){
    Console.WriteLine("Entre com a nota da N1: ");
    N1 = Convert.ToDouble(Console.ReadLine());
}
while (N2 > 0 && N2 < 10){
    Console.WriteLine("Entre com a nota da N2: ");
    N2 = Convert.ToDouble(Console.ReadLine());
}

double media = (N1 + N2) / 2;

if (media >= 7 && media <= 10)
{
    Console.WriteLine("Você está APROVADO!!");
}
else if (media < 7 && media > 3)
{
    Console.WriteLine("Você está de final!!");
}
else if (media < 3)
{
    Console.WriteLine("Você está REPROVADO!!");
}



