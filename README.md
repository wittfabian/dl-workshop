# Workshop am Herbstcampus 2017
### Dark Science mit Deep Learning: Einführung in modernes Maschinelles Lernen mit Python
Es gibt Probleme, die sind so komplex, dass das Ausprogrammieren deren Lösung entweder viel zu teuer oder momentan unmöglich wäre.
Ziel von Maschinellem Lernen (ML) als Disziplin der Künstlichen Intelligenz (KI) ist es, solche Probleme zu bewältigen, indem Systeme in erster Linie nicht programmiert, sondern trainiert werden.
Deep Learning (DL) als Teilgebiet des ML verwendet sog. tiefe neuronale Netze.
Neu ist dieser Ansatz nicht.
Neu ist hingegen der Erfolg, den heutzutage die schier grenzenlose Masse an verfügbaren Daten und die unbändige Rechenleistung möglich machen.

Mit TensorFlow und Keras bietet sich jetzt die Möglichkeit, diese hoch komplexen Netze mit wenig Aufwand zu definieren.

## Vorbereitung

1. Installieren Sie die Python-Distribution Anaconda: https://www.continuum.io/downloads (Python 3).
2. Erstellen Sie ein Conda Environment ([Hilfe](https://conda.io/docs/using/envs.html)) mit Hilfe der Datei `environment.yml`.
    * `conda env create -f environment.yml`
3. Installieren Sie TensorFlow ([Anleitung](https://www.tensorflow.org/install/)). 
    * Bitte nutzen Sie die Version **TensorFlow with CPU support only**
    * Es gibt eine extra Anleitung für die Installation mit der Python-Distribution Anaconda: **Installing with Anaconda**
4. Überprüfen Sie Ihre Installation
    * Aktivieren Sie ihr Environment: **activate tensorflow**
    * Rufen Sie das Testprogramm auf: **$ python tensorflow-test.py**
    * Sie sollten die folgenden Ausgaben sehen: 
        * Hello, TensorFlow!
        * TensorFlow version: 1.1.0
        * Ran 4 tests in XXXs OK
    * Warnungen können Sie ignorieren
    
## Agenda
* Einrichtung der Entwicklungsumgebung
* Grundlagen zum Thema Künstliche Intelligenz, Maschinelles Lernen und Deep Learning
* [Tensorflow](https://www.tensorflow.org/) & [Keras](https://keras.io/)
* Übungen
   * Arbeiten mit Daten
   * Vorhersage mit Feed-Forward-Netzen
   * Klassifikation von Bilddaten (Convolutional-Netz)

## Zeitlicher Ablauf
* ab 8.40: Registrierung und Begrüßungskaffee
* 9.40: Beginn
* 11.00 - 11.15: Kaffeepause
* 13.00 - 14.00: Mittagspause
* 16.00 - 16.30: Kaffeepause
* ca. 18.30 Uhr: Ende
    
    
## Fragen & Hilfe
Sollten Sie Fragen zur Installation, Vorbereitung oder zum Workshop selbst haben, können Sie sich jederzeit an mich wenden: fabian.witt@redheads.de

## Dozenten
### Fabian Witt
Fabian Witt hat seinen Master in Data & Knowledge Engineering an der Otto-von-Guericke-Universität Magdeburg gemacht. 
In dieser Zeit hat er sich speziell mit Themen wie Maschinellem Lernen, Data Mining und Schwarmintelligenz befasst.
Bei der Firma [Redheads Ltd.](https://www.redheads.de/) ist er als Technical Lead für den Bereich Data Science verantwortlich.

### Christopher Kraushaar
Christopher Kraushaar hat 2015 den praktischen Teil seiner Ausbildung zum Fachinformatiker für Anwendungsentwicklung bei Redheads absolviert. 
Seitdem gilt sein Interesse allen Themen im Zusammenhang mit Künstlicher Intelligenz und Machine Learning.
Derzeit arbeitet er bei [Redheads Ltd.](https://www.redheads.de/) und ist Teil des Teams bei [Rainforest Connection](https://rfcx.org/).
