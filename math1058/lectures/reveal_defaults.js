Reveal.initialize({
  width: 1536,
  height: 960,
  margin: 0.04,
  controls: false,
  progress: true,
  center: true,
  hash: true,
  transition: 'none',
  pdfSeparateFragments: true,
  // Learn about plugins: https://revealjs.com/plugins/
  plugins: [ RevealZoom, RevealNotes, RevealSearch, RevealMarkdown, RevealHighlight, RevealMath.KaTeX, RevealSpotlight ],
  spotlight: {
    presentingCursor: 'default',
    useAsPointer: true,
    size: 10,
    toggleSpotlightOnMouseDown: false,
    spotlightOnKeyPressAndHold: true,
  },
  keyboard: {
    // alternative to toggleSpotlightOnMouseDown:
    // toggle spotlight by pressing key 'c'
    67: function() { RevealSpotlight.toggleSpotlight() },
  },
});
