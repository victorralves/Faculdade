double N1 = 0;
double N2 = 0;

while (true)
{
    Console.WriteLine("Entre com a nota da N1: ");
    N1 = Convert.ToDouble(Console.ReadLine());
    if(N1 >= 0 && N1 <= 10)
    {
        break;
    }
    else
    {
        Console.WriteLine("\nEntrou com uma nota inválida!");
    }
}
while (true)
{
    Console.WriteLine("\nEntre com a nota da N2: ");
    N2 = Convert.ToDouble(Console.ReadLine());
    if (N2 >= 0 && N2 <= 10)
    {
        break;
    }
    else
    {
        Console.WriteLine("\nEntrou com uma nota inválida!");
    }
}

double media = (N1 + N2) / 2;

if (media >= 7 && media <= 10)
{
    Console.WriteLine($"\nSua média foi: {media}. \nVocê está APROVADO!!");
}
else if (media < 7 && media > 3)
{
    Console.WriteLine($"\nSua média foi: {media}. \nVocê está de final!!");
}
else if (media < 3)
{
    Console.WriteLine($"\nSua média foi: {media}. \nVocê está REPROVADO!!");
}