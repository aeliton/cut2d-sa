#!/bin/bash

mkdir -p results

rm -rf tex/article/results.tex
echo "
\\begin{center}
    \\resizebox{\textwidth}{!}{%
    \\begin{tabular}{ |c|c|c|c|c|c|c|c|c|}
    \\hline
        \\# & Instancia & \\# de Itens & Tam. Placa & S. Inicial & S. Média & S. Melhor & Desperdício & Tempo (s) \\\\ \\hline
" > tex/article/table.tex

COUNT=0
for file in $(ls input/* | sed 's/input\///;s/.txt$//'); do
    ITERATION=0
    COUNT=$(echo $COUNT + 1 | bc) 
    LOW=100
    FOLDER="results/$file"
    rm -rf $FOLDER
    for i in 1 2 3; do
        mkdir -p $FOLDER/$i
        pushd "${FOLDER}/${i}"
            DATA=$(../../../cut2d.py < ../../../input/"${file}.txt")
            echo $DATA
            PERCENT=$(echo $DATA| sed 's/\\.*//')
            N=$(echo $DATA| cut -d' ' -f 2)
            AREA=$(echo $DATA| cut -d' ' -f 3)
            INITIAL=$(echo $DATA| cut -d' ' -f 4)
            AVERAGE=$(echo $DATA| cut -d' ' -f 5)
            BEST=$(echo $DATA| cut -d' ' -f 6)
            TIME=$(echo $DATA| cut -d' ' -f 7)
            PIECES=$(echo $DATA| sed 's/.*\({.*}\)/\1/')
            echo $PERCENT
            if [ "$(echo $PERCENT'<'$LOW | bc -l)" -eq "1" ]; then
                ITERATION=$i
                LOW=$PERCENT
                LOW_DATA="Solução: $BEST, desperdício de $PERCENT\% de $AREA"
                TABLE="        $COUNT & $file & $N & $AREA & $INITIAL & $AVERAGE & $BEST & $PERCENT & $TIME \\\\ \\hline"
            fi
        popd
    done
    echo $TABLE >> tex/article/table.tex

echo "
\\begin{figure}
\\centering
\\begin{subfigure}{.5\\textwidth}
  \\centering
  \\includegraphics[width=1\\linewidth]{results/$file/$ITERATION/plot}
  \\label{fig:sub1}
\\end{subfigure}%
\\begin{subfigure}{.5\\textwidth}
  \\centering
  \\includegraphics[width=1\\linewidth]{results/$file/$ITERATION/cut}
  \\label{fig:sub2}
\\end{subfigure}
\\caption{Instancia $file.txt, $LOW_DATA, $PIECES}
\\label{fig:test}
\\end{figure}
" >> tex/article/results.tex
done

rm -rf tex/article/results
mv results tex/article/results

echo "
    \end{tabular}}
\end{center}
" >> tex/article/table.tex
