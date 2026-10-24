# Chaque demande latexmk actualise les figures Python avant l'exécution de pdfLaTeX.
# Le générateur ne relance Matplotlib que si un script, le style ou la palette a changé.
$pdf_mode = 1;
$go_mode = 1;
my $python = $ENV{'PYTHON'};
if (!$python && $ENV{'USERPROFILE'}) {
    my $bundled_python = $ENV{'USERPROFILE'}
        . '/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe';
    $python = $bundled_python if -f $bundled_python;
}
$python ||= 'python';
$pdflatex = "\"$python\" scripts/compile_with_figures.py %O %S";
