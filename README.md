# Dark Science with Deep Learning: Einführung in modernes Maschinelles Lernen mit Python
Es gibt Probleme, die sind so komplex, dass das Ausprogrammieren deren Lösung entweder viel zu teuer oder momentan unmöglich wäre.
Ziel von Maschinellem Lernen (ML) als Disziplin der Künstlichen Intelligenz (KI) ist es, solche Probleme zu bewältigen, indem Systeme in erster Linie nicht programmiert, sondern trainiert werden.
Deep Learning (DL) als Teilgebiet des ML verwendet sog. tiefe neuronale Netze.
Neu ist dieser Ansatz nicht.
Neu ist hingegen der Erfolg, den heutzutage die schier grenzenlose Masse an verfügbaren Daten und die unbändige Rechenleistung möglich machen.

Mit TensorFlow und Keras bietet sich jetzt die Möglichkeit, diese hoch komplexen Netze mit wenig Aufwand zu definieren.

## Vorbereitung

1. Installieren Sie die Python-Distribution Anaconda: https://www.anaconda.com/download/ (Python 3).
2. Laden Sie das GitHub-Repo herunter (Als ZIP oder via git)
3. Navigieren Sie zum Repo-Ordner (dl-workshop)
4. Erstellen Sie ein Conda Environment ([Hilfe](https://conda.io/docs/using/envs.html)) mit Hilfe der Datei `environment.yml`.
    * `$ conda env create -f environment.yml`
    * Alternativ können Sie das Environment im Anaconda Navigator unter "Environments > Import (unten)" mit Hilfe der `environment.yml` Datei importieren
5. Überprüfen Sie Ihre Installation
    * Aktivieren Sie ihr Environment: **$ activate dl-workshop**
    * Rufen Sie das Testprogramm unter `test/` auf: **$ python tensorflow-test.py**
    * Sie sollten die folgenden Ausgaben sehen: 
        * Hello, TensorFlow!
        * TensorFlow version: 1.3.0
        * Ran 4 tests in XXXs OK
    * Warnungen können Sie ignorieren
    * Bei Fragen oder Problemen schreiben Sie mir eine E-Mail

### Probleme bei der Installation 
* Wenn Sie einen Proxy verwenden, können Probleme bei der Installation auftreten!!
   * https://stackoverflow.com/questions/29267646/how-to-enable-proxy-servers-with-anaconda-python
   * https://stackoverflow.com/questions/36729023/how-to-make-anaconda-work-behind-http-proxy-not-https
   * Setzen Sie den pip-proxy und erstellen Sie die `.condarc`-Datei
   * Beenden Sie danach unbedingt die Session im Terminal und nutzen eine neue!
    
## Öffen des Projekts mit Jupyter Notebook

**Falls das Projekt (dl-workshop) auf einer anderen Festplatte abgelegt ist als die Anaconda-Installation:**
* https://stackoverflow.com/questions/35254852/how-to-change-jupyter-start-folder
* Beispieländerung: `c.NotebookApp.notebook_dir = 'D:\Source\python\dl-workshop'` (Pfadanpassen)

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
   * Einführung & Arbeiten mit Daten
   * Vorhersage mit Feed-Forward-Netzen
   * Klassifikation von Bilddaten ([Convolutional Neural Networks - CNNs / ConvNets](http://cs231n.github.io/convolutional-networks/))
   * Autoencoder
   * [Rekurrente neuronale Netze](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
* Optional:
   * Parameter-Tuning
   * Custom Layers
   * Multi Modal Networks
   * ...

## Grundlagen
### Neuronale Netze
* [How the backpropagation algorithm works](http://neuralnetworksanddeeplearning.com/chap2.html)
* [List of activation functions (equations)](https://stats.stackexchange.com/questions/154879/a-list-of-cost-functions-used-in-neural-networks-alongside-applications)
* [Comparison of activation functions](https://en.wikipedia.org/wiki/Activation_function)

### Convolutional Neural Networks
* [Convolutional Neural Networks](http://cs231n.github.io/convolutional-networks/)

### Rekurrente neuronale Netze
* [Rekurrente neuronale Netze](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
* [Stateful LSTM in Keras](http://philipperemy.github.io/keras-stateful-lstm/)
* [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)

### Autoencoders
* [Autoencoders in Keras](https://blog.keras.io/building-autoencoders-in-keras.html)

## Hilfreiche Links:
* [Jupyter Notebook Keyboard Shortcuts](https://www.cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/)
* [Managing Conda Environments](https://conda.io/docs/using/envs.html)
* [Tensorflow Playground](http://playground.tensorflow.org/)
* [NN & DL Glossary](https://deeplearning4j.org/glossary)
* [Comparing Top Deep Learning Frameworks](https://deeplearning4j.org/compare-dl4j-torch7-pylearn)
* [Deep Learning Cheat Sheet](https://github.com/kailashahirwar/cheatsheets-ai/blob/master/PDFs/Deep%20Learning%20Cheat%20Sheet-Hacker%20Noon.pdf)
* [When not to use deep learning](http://hyperparameter.space/blog/when-not-to-use-deep-learning/)
* [List of activation functions (equations)](https://stats.stackexchange.com/questions/154879/a-list-of-cost-functions-used-in-neural-networks-alongside-applications)
* [Comparison of activation functions](https://en.wikipedia.org/wiki/Activation_function)
* [L1, L2 & Max Normalization](https://stats.stackexchange.com/questions/225564/scikit-learn-normalization-mode-l1-vs-l2-max)
* [Open Data for Deep Learning](https://deeplearning4j.org/opendata)
* [First contact with TensorFlow](http://jorditorres.org/research-teaching/tensorflow/first-contact-with-tensorflow-book/first-contact-with-tensorflow/)
* [Overview of gradient descent optimization algorithms](http://ruder.io/optimizing-gradient-descent/)

## Fragen & Hilfe
Sollten Sie Fragen zur Installation, Vorbereitung oder zum Workshop selbst haben, können Sie sich jederzeit an mich wenden: fabian.witt@redheads.de

## Dozent
### Fabian Witt
Fabian Witt hat seinen Master in Data & Knowledge Engineering an der Otto-von-Guericke-Universität Magdeburg gemacht. 
In dieser Zeit hat er sich speziell mit Themen wie Maschinellem Lernen, Data Mining und Schwarmintelligenz befasst.
Bei der Firma [Redheads Ltd.](https://www.redheads.de/) ist er als Technical Lead für den Bereich Data Science verantwortlich.
