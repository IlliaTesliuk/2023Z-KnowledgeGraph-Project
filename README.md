# 2023Z-KnowledgeGraph-Project

<p>Project 13A. Transform any static dataset to a knowledge graph with RML<br>
Author: Illia Tesliuk</p>

## Instructions

1. Make sure you have a recent version of Node.js installed.

2. Install the yarrrml-parser, which translates YARRRML rules to RML rules.
```
npm i @rmlio/yarrrml-parser -g
```

3. Make sure you have a recent version of Java installed.

4. Make sure you have a recent version of the RMLMapper (https://github.com/RMLio/rmlmapper-java). You can either download a release or build it from source.

5. Translate the YARRRML rules into RML file 
```
yarrrml-parser -i mappings/rules_comb.yml -o mappings/rules_comb.rml.ttl
```

6. Execute the RMLMapper with the corresponding RML rules.
```
java -jar /path/to/rmlmapper.jar -m mappings/rules_comb.rml.ttl -o outputs/spotify.ttl 
```

## Structure

### spotify songs
<p>Contains an open "Spotify Songs" dataset split into 5 CSV files for artists, albums, genres, songs and playlists. </p>

### mappings
<p>Contains a custom Spotify ontology, YAML mapping rules and the resulting RML mapping.</p>

### outputs
<p>Contains the resulting Spotify dataset in RDF format</p>
