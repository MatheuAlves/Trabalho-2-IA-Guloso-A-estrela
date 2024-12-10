# Trabalho 2 - Inteligência Artificial

Participantes: Matheus Alves e Pablo Sousa

## Contextualização
O trabalho apresentado tem como objetivo implementar e comparar o desempenho de dois algoritmos de busca (A* e Busca Gulosa) aplicados ao problema clássico de labirinto. A atividade visa avaliar aspectos de desempenho como tempo de execução, consumo de memória, completude e optimalidade dos algoritmos escolhidos. A partir desses resultados, busca-se analisar e discutir por que determinados algoritmos apresentam vantagens em certas métricas e condições do problema, oferecendo uma compreensão mais profunda das técnicas de busca na área de Inteligência Artificial.

---

## 🧑‍💻 1. Implementação
Os dois algoritmos foram implementados com as seguintes características principais:

- **A***:
  - Utiliza a soma do custo acumulado até o nó atual g(n) e da heurística h(n) para priorizar os nós, calculando f(n) = g(n) + h(n).
  - Garante a melhor solução possível, se houver uma, desde que a heurística seja admissível (não superestima o custo real).
  - No código, os nós são priorizados ao ordenar uma lista com base no menor valor de f(n), permitindo explorar os caminhos mais promissores primeiro.

  
- **Busca Gulosa**:
  - Prioriza exclusivamente os nós com menor valor heurístico h(n), ignorando o custo acumulado g(n).
  - Pode ser mais eficiente em termos de tempo e memória, já que não mantém informações detalhadas sobre o custo acumulado. No entanto, pode não encontrar o caminho mais curto, pois considera apenas a proximidade ao objetivo, sem avaliar o custo total do caminho.
  - No código, os nós são priorizados ao ordenar uma lista com base no menor valor de h(n), explorando os nós aparentemente mais próximos do objetivo.


---

## 📊 2. Medições de Desempenho

Para avaliar os algoritmos, foram medidas as seguintes métricas:
- **Tempo de Execução**: Eficiência do algoritmo em termos de velocidade.
- **Consumo de Memória**: Memória usada para armazenar dados durante a execução.
- **Completude**: Habilidade do algoritmo de sempre encontrar um caminho, se ele existir.
- **Optimalidade**: Verifica se o algoritmo encontra o menor caminho.

## 📈 3. Resultados e Análise Comparativa

| Métrica             | A*                   | Busca Gulosa                      |
|---------------------|-----------------------|--------------------------|
| Tempo de Execução   | 0.0018858999 segundos | 0.0002143000 segundos    |
| Consumo de Memória  | 2.41 KB; Pico: 2.82 KB| A*: 0.84 KB; Pico: 0.91 KB   |
| Completude          | Completo              | Completo                 |
| Optimalidade        | Ótimo (menor caminho) | Não garante menor caminho|

---

## 📈 3. Análise dos Resultados

1. **Tempo de Execução**:
   - A Busca Gulosa foi mais rápida, pois realiza menos verificações ao priorizar exclusivamente o valor heurístico. 
   - A* é mais lento porque mantém informações de custo acumulado e reprocessa nós se necessário.

2. **Consumo de Memória**:
   - A Busca Gulosa consome menos memória, já que não armazena informações detalhadas como o custo acumulado. No entanto, em alguns casos, o consumo pode ser semelhante devido ao armazenamento de nós na lista de exploração.
   - A* utiliza memória adicional para manter o custo acumulado de cada nó.

3. **Completude**:
   - O A* é completo, garantindo que encontrará uma solução, caso ela exista, desde que o espaço de busca seja finito ou a heurística seja admissível.
   - A Busca Gulosa pode não ser completa em casos específicos, como quando há ciclos ou desvios causados pela priorização exclusiva da heurística.

4. **Optimalidade**:
   - A* é ótimo, sempre encontrando o menor caminho possível.
   - Busca Gulosa, por ignorar o custo acumulado, pode retornar caminhos mais longos.

---

## 💻 4. Conclusão e Sugestões de Melhorias

- **A*** é mais robusto e adequado para problemas onde a qualidade da solução (caminho mais curto) é crucial. O custo em tempo e memória é justificado por sua optimalidade.
- **Busca Gulosa** é útil quando o tempo e a memória são limitados, e uma solução subótima é aceitável.

### Possíveis Melhorias

- Para **A***:
  - Tornar a heurística mais inteligente e capaz de se ajustar durante a execução pode ajudar a resolver problemas mais rapidamente em situações específicas.
  
- Para **Busca Gulosa**:
  - Incluir uma checagem extra para considerar o custo acumulado em pontos importantes pode melhorar a qualidade do caminho encontrado, tornando-o mais eficiente.
