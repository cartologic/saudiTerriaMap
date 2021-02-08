import React from "react";
import { useTranslation } from "react-i18next";
import i18next from "i18next";

const changeLanguage = () => e => {
  const code = localStorage.getItem("i18nextLng"); // Either 'ar' or 'en'
  if (code === "ar") {
    localStorage.setItem("i18nextLng", "en");
  } else {
    localStorage.setItem("i18nextLng", "ar");
  }
  window.location.reload();
};

const ToggleLanguage = () => {
  const { t } = useTranslation();
  document.body.dir = i18next.dir();

  return (
    <div className="tjs-panel__panel">
      <button
        type="button"
        className="tjs-panel__button tjs-_buttons__btn tjs-_buttons__btn--map"
        title={t("translate.title")}
        onClick={changeLanguage()}
      >
        <span>{t("translate.text")}</span>
      </button>
    </div>
  );
};

export default ToggleLanguage;
