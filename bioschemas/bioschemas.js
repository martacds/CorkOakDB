/**
GENERAL
**/

let fullURL = window.location.href;
let baseURL = "https://corkoakdb.org/";

let title = document.title;
let id = fullURL;

let geneURL = baseURL + "gene/";
let protURL = baseURL + "polypeptide/";
let taxonURL = baseURL + "corkoak";
let dataURL = baseURL + "Analysis/";
let sampURL = baseURL + "biologicalsample/";
let blastURL = baseURL + "jbrowse";
let jbrowURL = baseURL + "blast";
let mapURL = baseURL + "heatmap";

/**
IF/ELSE
**/

if(fullURL.startsWith(geneURL)) { //GENES
  let name = title.substring(0,12);
  let nr = title.substring(3,12); //for CrossRef link
  let alternateName = "gene-" + name; //gene-LOC
  let sameAs = "https://www.ncbi.nlm.nih.gov/gene/?term=" + nr; //link Cross Reference

  let json1 = String("\{\"\@context\"\:\"http\:\/\/schema\.org\"\,\"\@id\"\:\"");
  let json2 = String("\"\,\"\@type\"\:\"Gene\"\,\"alternateName\"\:\[\"");
  let json3 = String("\"\]\,\"dct\:conformsTo\"\:\"https\:\/\/bioschemas\.org\/profiles\/Gene\/0\.7\-RELEASE\"\,\"identifier\"\:\"");
  let json4 = String("\"\,\"name\"\:\"");
  let json5 = String("\"\,\"sameAs\"\:\[\"");
  let json6 = String("\"\]\,\"taxonomicRange\"\:\[\{\"\@context\"\:\"http\:\/\/schema\.org\"\,\"\@type\"\:\"Taxon\"\,\"dct\:conformsTo\"\:\"https\:\/\/bioschemas\.org\/profiles\/Taxon\/0\.6\-RELEASE\"\,\"name\"\:\"Quercus suber\"\}\]\,\"url\"\:\"");
  let json7 = String("\"\}");

  let jsonADD = json1 + id + json2 + alternateName + json3 + id + json4 + name + json5 + sameAs + json6 + id + json7;
  let obj = JSON.parse(jsonADD);

  let e = document.createElement('script');
  e.text = JSON.stringify(obj),
  e.type = 'application/ld+json',
  e.id = 'dataRecord',
  e.async = !0,
  document.getElementsByTagName('head') [0].appendChild(e)


} else if(fullURL.startsWith(protURL)) { //POLYPEPTIDES
  let name = title.substring(0,14);
  let alternateName = "polypeptide-" + name; //polypeptide-XP
  let sameAs = "https://www.ncbi.nlm.nih.gov/search/all/?term=" + name; //link Cross Reference

  let json1 = String("\{\"\@context\"\:\"http\:\/\/schema\.org\"\,\"\@id\"\:\"");
  let json2 = String("\"\,\"\@type\"\:\"Protein\"\,\"alternateName\"\:\[\"");
  let json3 = String("\"\]\,\"dct\:conformsTo\"\:\"https\:\/\/bioschemas\.org\/profiles\/Protein\/0\.11\-RELEASE\"\,\"identifier\"\:\"");
  let json4 = String("\"\,\"name\"\:\"");
  let json5 = String("\"\,\"sameAs\"\:\[\"");
  let json6 = String("\"\]\,\"taxonomicRange\"\:\[\{\"\@context\"\:\"http\:\/\/schema\.org\"\,\"\@type\"\:\"Taxon\"\,\"dct\:conformsTo\"\:\"https\:\/\/bioschemas\.org\/profiles\/Taxon\/0\.6\-RELEASE\"\,\"name\"\:\"Quercus suber\"\}\]\,\"url\"\:\"");
  let json7 = String("\"\}");

  let jsonADD = json1 + id + json2 + alternateName + json3 + id + json4 + name + json5 + sameAs + json6 + id + json7;
  let obj = JSON.parse(jsonADD);

  let e = document.createElement('script');
  e.text = JSON.stringify(obj),
  e.type = 'application/ld+json',
  e.id = 'dataRecord',
  e.async = !0,
  document.getElementsByTagName('head') [0].appendChild(e)


} else if(fullURL.startsWith(sampURL)) { //BIOSAMPLES
  let name = title.substring(0,9);

  let json1 = String("\{\"\@context\"\:\"http\:\/\/schema\.org\"\,\"\@id\"\:\"");
  let json2 = String("\"\,\"\@type\"\:\"Sample\"\,\"dct\:conformsTo\"\:\"https\:\/\/bioschemas\.org\/profiles\/Sample\/0\.2\-RELEASE\-2018\_11\_10\"\,\"identifier\"\:\[\"");
  let json3 = String("\"\]\,\"name\"\:\[\"");
  let json4 = String("\"\]\,\"url\"\:\"");
  let json5 = String("\"\}");

  let jsonADD = json1 + id + json2 + id + json3 + name + json4 + id + json5;
  let obj = JSON.parse(jsonADD);

  let e = document.createElement('script');
  e.text = JSON.stringify(obj),
  e.type = 'application/ld+json',
  e.id = 'dataRecord',
  e.async = !0,
  document.getElementsByTagName('head') [0].appendChild(e)


} else if(fullURL.startsWith(dataURL)) { //BIOPROJECTS
  let name = title.substring(0,9);
  let description = "This dataset can be consulted at https://www.ncbi.nlm.nih.gov/bioproject/" + name;

  let json1 = String("\{\"\@context\"\:\"http\:\/\/schema\.org\"\,\"\@id\"\:\"");
  let json2 = String("\"\,\"\@type\"\:\"Dataset\"\,\"dct\:conformsTo\"\:\"https\:\/\/bioschemas\.org\/profiles\/Dataset\/0\.3\-RELEASE\-2019\_06\_14\"\,\"description\"\:\"");
  let json3 = String("\"\,\"identifier\"\:\[\"");
  let json4 = String("\"\]\,\"keywords\"\:\[\]\,\"name\"\:\"");
  let json5 = String("\"\,\"url\"\:\"");
  let json6 = String("\"\}");

  let jsonADD = json1 + id + json2 + description + json3 + id + json4 + name + json5 + id + json6;
  let obj = JSON.parse(jsonADD);

  let e = document.createElement('script');
  e.text = JSON.stringify(obj),
  e.type = 'application/ld+json',
  e.id = 'dataRecord',
  e.async = !0,
  document.getElementsByTagName('head') [0].appendChild(e)

} else if(fullURL.startsWith(taxonURL)) { //ORGANISM

  let json1 = String("\{\"\@context\"\:\"http\:\/\/schema\.org\"\,\"\@id\"\:\"https\:\/\/corkoakdb\.org\/corkoak\"\,\"\@type\"\:\"Taxon\"\,\"alternateName\"\:\[\"Cork Oak\"\]\,\"childTaxon\"\:\[\{\"\@context\"\:\"http\:\/\/schema\.org\"\,\"\@type\"\:\"Taxon\"\,\"dct\:conformsTo\"\:\"https\:\/\/bioschemas\.org\/profiles\/Taxon\/0\.6\-RELEASE\"\,\"name\"\:\"Quercus suber\"\,\"taxonRank\"\:\[\"txid58331\"\,\"species\"\]\}\]\,\"dct\:conformsTo\"\:\"https\:\/\/bioschemas\.org\/profiles\/Taxon\/0\.6\-RELEASE\"\,\"name\"\:\"Quercus suber\"\,\"parentTaxon\"\:\{\"\@context\"\:\"http\:\/\/schema\.org\"\,\"\@type\"\:\"Taxon\"\,\"dct\:conformsTo\"\:\"https\:\/\/bioschemas\.org\/profiles\/Taxon\/0\.6\-RELEASE\"\,\"name\"\:\"Quercus\"\,\"taxonRank\"\:\[\"txid3511\"\,\"genus\"\]\}\,\"taxonRank\"\:\[\"txid58331\"\,\"species\"\]\,\"url\":\"https\:\/\/corkoakdb\.org\/corkoak\"\}");

  let jsonADD = json1;
  let obj = JSON.parse(jsonADD);

  let e = document.createElement('script');
  e.text = JSON.stringify(obj),
  e.type = 'application/ld+json',
  e.id = 'dataRecord',
  e.async = !0,
  document.getElementsByTagName('head') [0].appendChild(e)

}
