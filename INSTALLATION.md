# Einrichten der Entwicklungsumgebung

* [Installation auf dem PC](#installation-auf-dem-pc)
* [Installation via Docker](docker/README.md)


## Installation auf dem PC

1. Installieren Sie die Python-Distribution Anaconda: https://www.anaconda.com/download/ (Python 3).
2. Laden Sie das GitHub-Repo herunter (als ZIP wird empfohlen)
3. Navigieren Sie zum Repo-Ordner (dl-workshop)
4. Erstellen Sie ein Conda Environment ([Hilfe](https://conda.io/docs/using/envs.html)) mit Hilfe der Datei `environment.yml`.
    * `$ conda env create -f environment.yml`
    * Alternativ können Sie das Environment im Anaconda Navigator unter "Environments > Import (unten)" mit Hilfe der `environment.yml` Datei importieren
5. Überprüfen Sie Ihre Installation im Terminal
    * Aktivieren Sie Ihr Environment: **$ activate dl-workshop**
    * Rufen Sie das Testprogramm unter `test/` auf: **$ python tensorflow-test.py**
    * Sie sollten die folgenden Ausgaben sehen: 
        * Hello, TensorFlow!
        * TensorFlow version: 1.4.0
        * Ran 4 tests in XXXs OK
    * Warnungen können Sie ignorieren
    * Bei Fragen oder Problemen schreiben Sie einfach eine E-Mail

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
1. Aktivieren Sie Ihr Environment: **$ activate dl-workshop**
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