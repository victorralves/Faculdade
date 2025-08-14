Console.WriteLine("Entre com a sua idade: ");
double idade = Convert.ToDouble(Console.ReadLine());

if (idade < 12)
{
    Console.WriteLine("\nVocê é uma CRIANÇA!");
}
else if(idade >= 12 && idade < 18)
{
    Console.WriteLine("\nVocê é um ADOLESCENTE!");
}
else if(idade >= 18)
{
    Console.WriteLine("\nVocê é um ADULTO!");
}

