(function () {
  const navigator = window.navigator;
  const screen = window.screen;

  let data = {
    navigator: {
      userAgent: navigator.userAgent,
      userLanguage: navigator.userLanguage,
      vendor: navigator.vendor,
      language: navigator.language,
      platform: navigator.platform,
      appName: navigator.appName,
      appVersion: navigator.appVersion,
    },
    screen: {
      availWidth: screen.availWidth,
      availHeight: screen.availHeight,
    },
  };
  console.log(JSON.stringify(data));
})();
