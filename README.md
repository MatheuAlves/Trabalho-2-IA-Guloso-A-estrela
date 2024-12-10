# Trabalho 2 - Inteligência Artificial

Participantes: Matheus Alves e Pablo Sousa

## Contextualização
O trabalho apresentado tem como objetivo implementar e comparar o desempenho de dois algoritmos de busca (A* e Busca Gulosa) aplicados ao problema clássico de labirinto. A atividade visa avaliar aspectos de desempenho como tempo de execução, consumo de memória, completude e optimalidade dos algoritmos escolhidos. A partir desses resultados, busca-se analisar e discutir por que determinados algoritmos apresentam vantagens em certas métricas e condições do problema, oferecendo uma compreensão mais profunda das técnicas de busca na área de Inteligência Artificial.

---

## 🧑‍💻 1. Implementação
Os dois algoritmos foram implementados com as seguintes características principais:

- **A***:
  - Utiliza a soma do custo acumulado até o nó atual e da heurística para priorizar os nós.
  - Garante a melhor solução possível, se existente.
  
- **Busca Gulosa**:
  - Prioriza exclusivamente os nós com menor valor heurístico, ignorando o custo acumulado.
  - Mais eficiente em termos de memória, mas pode não encontrar o caminho mais curto.

Ambos utilizam uma fila de prioridade (`heapq`) para explorar os nós e verificam a validade do movimento para evitar obstáculos.

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
   - A Busca Gulosa consome menos memória, pois armazena menos informações no caminho.
   - A* utiliza memória adicional para manter o custo acumulado de cada nó.

3. **Completude**:
   - Ambos os algoritmos são completos, garantindo que encontrarão uma solução, caso ela exista.

4. **Optimalidade**:
   - A* é ótimo, sempre encontrando o menor caminho possível.
   - Busca Gulosa, por ignorar o custo acumulado, pode retornar caminhos mais longos.

---

## 💻 4. Conclusão e Sugestões de Melhorias

- **A*** é mais robusto e adequado para problemas onde a qualidade da solução (caminho mais curto) é crucial. O custo em tempo e memória é justificado por sua optimalidade.
- **Busca Gulosa** é útil quando o tempo e a memória são limitados, e uma solução subótima é aceitável.

### Possíveis Melhorias

- Para **A***:
  - Implementar uma heurística adaptativa que ajusta dinamicamente os custos pode reduzir o tempo de execução em cenários específicos.
  
- Para **Busca Gulosa**:
  - Combinar com uma validação de custo acumulado em nós críticos pode melhorar a qualidade do caminho encontrado.
