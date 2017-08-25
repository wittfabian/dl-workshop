# [Workshop am Herbstcampus 2017](https://www.herbstcampus.de/programm.php)
### Dark Science mit Deep Learning: Einführung in modernes Maschinelles Lernen mit Python
Es gibt Probleme, die sind so komplex, dass das Ausprogrammieren deren Lösung entweder viel zu teuer oder momentan unmöglich wäre.
Ziel von Maschinellem Lernen (ML) als Disziplin der Künstlichen Intelligenz (KI) ist es, solche Probleme zu bewältigen, indem Systeme in erster Linie nicht programmiert, sondern trainiert werden.
Deep Learning (DL) als Teilgebiet des ML verwendet sog. tiefe neuronale Netze.
Neu ist dieser Ansatz nicht.
Neu ist hingegen der Erfolg, den heutzutage die schier grenzenlose Masse an verfügbaren Daten und die unbändige Rechenleistung möglich machen.

Mit TensorFlow und Keras bietet sich jetzt die Möglichkeit, diese hoch komplexen Netze mit wenig Aufwand zu definieren.

## Vorbereitung

1. Installieren Sie die Python-Distribution Anaconda: https://www.continuum.io/downloads (Python 3).
2. Laden Sie das GitHub-Repo herunter (Als ZIP oder via git)
3. Navigieren Sie zum Repo-Ordner (dl-workshop)
4. Erstellen Sie ein Conda Environment ([Hilfe](https://conda.io/docs/using/envs.html)) mit Hilfe der Datei `environment.yml`.
    * `$ conda env create -f environment.yml`
    * Alternativ können Sie das Environment im Anaconda Navigator unter "Environments > Import (unten)" mit Hilfe der `environment.yml` Datei importieren
5. Installieren Sie TensorFlow ([Anleitung](https://www.tensorflow.org/install/)). 
    * Schließen Sie PyCharm und alle anderen Programme die das Environment nutzen
    * Bitte nutzen Sie die Version **TensorFlow with CPU support only**
    * Es gibt eine extra Anleitung für die Installation mit der Python-Distribution Anaconda: **Installing with Anaconda**
6. Überprüfen Sie Ihre Installation
    * Aktivieren Sie ihr Environment: **$ activate dl-workshop**
    * Rufen Sie das Testprogramm unter `test/` auf: **$ python tensorflow-test.py**
    * Sie sollten die folgenden Ausgaben sehen: 
        * Hello, TensorFlow!
        * TensorFlow version: 1.3.0
        * Ran 4 tests in XXXs OK
    * Warnungen können Sie ignorieren
    * Bei Fragen oder Problemen schreiben Sie mir eine E-Mail
    
## Öffen des Projekts mit Jupyter Notebook

### Im Terminal
1. Aktivieren Sie ihr Environment: **$ activate dl-workshop**
2. Starten Sie Jupyter Notebook: **$ jupyter notebook**
3. Ein Browser-Fenster sollte sich automatisch öffnen, wenn nicht wird der Link im Terminal angezeigt

### Mit Anaconda Navigator
1. Starten sie das Programm Anaconda Navigator
2. Wählen sie unter "Home" das Environment "dl-workshop" aus (Select-Feld unter "Applications on")
3. Jupyter Notebook erscheint als Programm. Drücken Sie "Launch" um die Anwendung zu starten
4. Ein Browser-Fenster öffnet sich, unter dem Sie die Anwendung erreichen können

### Dateien öffnen
1. Im Browser-Fenster können Sie nun zum Projektordner (GitHub Repository) navigieren
2. Die Dateien mit der Endung ".ipynb" können mit der Anwendung geöffnet werden
    
## Agenda
* Einrichtung der Entwicklungsumgebung
* Grundlagen zum Thema Künstliche Intelligenz, Maschinelles Lernen und Deep Learning
* Grundlagen zu [Tensorflow](https://www.tensorflow.org/) & [Keras](https://keras.io/)
* Übungen
   * Arbeiten mit Daten
   * Vorhersage mit Feed-Forward-Netzen
   * Klassifikation von Bilddaten ([Convolutional Neural Networks - CNNs / ConvNets](http://cs231n.github.io/convolutional-networks/))
   * [Rekurrente neuronale Netze](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
   * Parameter-Tuning
   * Vorhersage von Zeitreihen

## Zeitlicher Ablauf
* ab 8.40: Registrierung und Begrüßungskaffee
* 9.40: Beginn
* 11.00 - 11.15: Kaffeepause
* 13.00 - 14.00: Mittagspause
* 16.00 - 16.30: Kaffeepause
* ca. 18.30 Uhr: Ende
    
    
## Fragen & Hilfe
Sollten Sie Fragen zur Installation, Vorbereitung oder zum Workshop selbst haben, können Sie sich jederzeit an mich wenden: fabian.witt@redheads.de

## Hilfreiche Links:
* [Jupyter Notebook Keyboard Shortcuts](https://www.cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/)
* [Managing Conda Environments](https://conda.io/docs/using/envs.html)
* [Tensorflow Playground](http://playground.tensorflow.org/)
* [NN & DL Glossary](https://deeplearning4j.org/glossary)
* [Comparing Top Deep Learning Frameworks](https://deeplearning4j.org/compare-dl4j-torch7-pylearn)
* [Deep Learning Cheat Sheet](https://github.com/kailashahirwar/cheatsheets-ai/blob/master/PDFs/Deep%20Learning%20Cheat%20Sheet-Hacker%20Noon.pdf)

## Dozent
### Fabian Witt
Fabian Witt hat seinen Master in Data & Knowledge Engineering an der Otto-von-Guericke-Universität Magdeburg gemacht. 
In dieser Zeit hat er sich speziell mit Themen wie Maschinellem Lernen, Data Mining und Schwarmintelligenz befasst.
Bei der Firma [Redheads Ltd.](https://www.redheads.de/) ist er als Technical Lead für den Bereich Data Science verantwortlich.
