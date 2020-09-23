(function () {
  let checkCookie = () => {
    return document.cookie.match(/^(.*;)?\s*<API_HOSTNAME>\s*=\s*[^;]+(.*)?$/);
  };

  let setCookie = () => {
    var d = new Date();
    d.setTime(d.getTime() + 7 * 24 * 60 * 60 * 1000);
    var expires = "expires=" + d.toUTCString();
    document.cookie =
      "<API_HOSTNAME>" +
      "=" +
      `data-submitted` +
      ";" +
      expires +
      ";path=/;SameSite=Lax";
  };

  if (!checkCookie("api.browser-research.com")) {
    const navigator = window.navigator;
    const screen = window.screen;

    let data = {
      navigator: {
        userAgent: navigator.userAgent,
        userLanguage: navigator.languages
          ? navigator.languages[0]
          : navigator.language || navigator.userLanguage,
        vendor: navigator.vendor,
        platform: navigator.platform,
        appName: navigator.appName,
        appVersion: navigator.appVersion,
      },
      clientTime: new Date(),
      clientTimezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
      screen: {
        availWidth: screen.availWidth,
        availHeight: screen.availHeight,
      },
      location: {
        href: location.href,
      },
    };

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "https://<API_HOSTNAME>/data/push", true);
    xhr.setRequestHeader("Content-Type", "application/json; charset=utf-8");
    xhr.send(JSON.stringify(data));

    setCookie();
  }
})();
