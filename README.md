Sääbotti on Facebookin wit.ai-alustan avulla tehty botti. Se ymmärtää sille luonnollisella kielellä annettuja pyyntöjä kertoa sää. Merkittävä osa tämän botin toiminnallisuudesta luodaan käyttämällä wit.ai:n verkkosivua osoitteessa wit.ai. 
 
Botti on kirjoitettu python-kielellä ja se käyttää hyväkseen wit.ai:n lisäksi voikko-nimistä työkalua. Voikon avulla saadaan sovellus “ymmärtämään” suomenkieltä, sillä wit.ai:n suomenkielen tuki on vielä vaiheessa. Voikon asentaminen on haastavaa ja helpoiten sen saa ubuntu-käyttöjärjestelmän mukana. Python valittiin sääbotin ohjelmointikieleksi, sillä sen avulla on helpohko kommunikoida voikon kanssa libvoikko-kirjaston avulla.
 
Asennettuasi voikon ja tarvittavat python kirjastot (requests, libvoikko) laita allaolevat tiedostot samaan kansioon ja ja aja weather.py komennolla python3 weather.py.

## Asennus suomenkielisellä ubuntu-käyttöjärjestelmällä (voikko tulee sisäänrakennettuna)

1. `pip install requests`
2. `apt-get install python-libvoikko`

## Aja koodia komennolla

`python3 weather.py`
