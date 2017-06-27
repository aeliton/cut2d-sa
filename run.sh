#!/bin/bash

mkdir -p results

rm -rf tex/article/results.tex

for file in $(ls input/* | sed 's/input\///;s/.txt$//'); do
    FOLDER="results/$file"
    rm -rf $FOLDER
    for i in 1 2 3; do
        mkdir -p $FOLDER/$i
        pushd "${FOLDER}/${i}"
            ../../../cut2d.py < ../../../input/"${file}.txt"
        popd
    done

echo "
\\begin{figure}
\\centering
\\begin{subfigure}{.5\\textwidth}
  \\centering
  \\includegraphics[width=1\\linewidth]{results/$file/1/plot}
  \\label{fig:sub1}
\\end{subfigure}%
\\begin{subfigure}{.5\\textwidth}
  \\centering
  \\includegraphics[width=1\\linewidth]{results/$file/1/cut}
  \\label{fig:sub2}
\\end{subfigure}
\\caption{Instancia $file.txt, x\%}
\\label{fig:test}
\\end{figure}
" >> tex/article/results.tex
done

rm -rf tex/article/results
mv results tex/article/results
