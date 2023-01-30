% vim: set spelllang=fr:
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{main}

%\PassOptionsToClass{t}{beamer}
\LoadClass{beamer}
\usetheme{Curse}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% > Paquetages

% Code et algos
\RequirePackage{minted}

% Langue
\RequirePackage{polyglossia}
\RequirePackage{csquotes}

% Figures
\RequirePackage{tikz}
\RequirePackage{graphicx}
\RequirePackage{ifdraft}
\RequirePackage{cutwin}
\RequirePackage{forest}

% Maths
\RequirePackage{amsmath}

% Tables
\RequirePackage{tabularx}
\RequirePackage{booktabs}

% Liens
\RequirePackage{hyperref}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% > Configuration

% Langue
\setmainlanguage{french}

% Figures
\usetikzlibrary{calc}
\usetikzlibrary{positioning}
\usetikzlibrary{decorations.pathreplacing}
\usetikzlibrary{decorations.markings}
\usetikzlibrary{arrows.meta}
\usetikzlibrary{shapes.symbols}

\pgfdeclarelayer{back}
\pgfsetlayers{back,main}

\tikzset{
    onslide/.code args={<#1>#2}{\only<#1>{\pgfkeysalso{#2}}}
}

\forestset{
    onslide/.code args={<#1>#2}{\only<#1>{\pgfkeysalso{#2}}}
}

% Raccourcis
\newcommand{\icl}{$\cdot$}
\newcommand{\minititle}[1]{{\scriptsize\rmfamily\MakeLowercase{#1}}\par\addvspace{.5em}}

% Maths
\DeclareMathOperator{\inv}{inv}
\DeclareMathOperator{\pgcd}{pgcd}
\DeclareMathOperator{\ppcm}{ppcm}