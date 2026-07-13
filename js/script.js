const translations = {
    en: {
        calameo_access: "Access to Calaméo<br>Digital Magazine",
        about: "About",
        features: "Features",
        story: "Our Story",
        magazine: "Digital Magazine",
        member: "Explore LIONESS",
        hero_title: "LIONESS, LE MAGAZINE DES REINES",
        hero_text1: "is much more than a magazine.",
        hero_text2: "Celebrating African and Afro-descendant women through stories, entrepreneurship and community.",
        hero_text3: "Joining LIONESS means becoming part of a community that celebrates women's ambitions and impact.",
        see_magazines: "See the magazines",
        discover: "Discover LIONESS",
        feature1: "Digital Magazine",
        feature1_desc: "Read every edition of LIONESS directly online through an intuitive digital reading experience.",
        feature2: "Women's Community",
        feature2_desc: "Create an account, connect with inspiring women, and become part of a growing international network.",
        feature3: "Stories & Inspiration",
        feature3_desc: "Discover authentic stories, interviews and entrepreneurial journeys from women making an impact worldwide.",
        about_title: "About LIONESS",
        about_story: "LIONESS was created to give greater visibility to African and Afro-descendant women whose achievements are too often overlooked. Inspired by the remarkable women I met while growing up in Gabon, I wanted to build more than a digital magazine—I wanted to create a space where women could inspire one another, connect, and celebrate their success.",
        about_story2: "Developed as my Holberton School Portfolio Project, LIONESS combines my passion for web development with my commitment to promoting women's leadership. Built with Django, Bootstrap, HTML, CSS, and JavaScript, it offers a modern, responsive, and accessible platform.",
        project_links: "Project Links",
        live_app: "Live Application",
        github: "GitHub Repository",
        demo: "Demo Video",
        navigation: "Navigation",
        portfolio: "Portfolio Project",
        portfolio_desc: "Developed as part of the Holberton School Portfolio Project."
    },
    fr: {
        calameo_access: "Accéder au magazine<br>numérique Calaméo",
        about: "À propos",
        features: "Fonctionnalités",
        story: "Notre histoire",
        magazine: "Magazine numérique",
        member: "Découvrir LIONESS",
        hero_title: "LIONESS, LE MAGAZINE DES REINES",
        hero_text1: "est bien plus qu'un magazine.",
        hero_text2: "Célébrer les femmes africaines et afro-descendantes à travers leurs histoires, leur entrepreneuriat et leur communauté.",
        hero_text3: "Rejoindre LIONESS, c'est intégrer une communauté qui célèbre les ambitions et l'impact des femmes.",
        see_magazines: "Découvrir les magazines",
        discover: "Découvrir LIONESS",
        feature1: "Magazine numérique",
        feature1_desc: "Lisez toutes les éditions de LIONESS en ligne grâce à une expérience de lecture intuitive.",
        feature2: "Communauté de femmes",
        feature2_desc: "Créez un compte, échangez avec des femmes inspirantes et rejoignez un réseau international.",
        feature3: "Histoires et inspirations",
        feature3_desc: "Découvrez des témoignages, des interviews et des parcours entrepreneuriaux inspirants.",
        about_title: "À propos de LIONESS",
        about_story: "LIONESS a été créé pour offrir une plus grande visibilité aux femmes africaines et afro-descendantes, dont les réussites sont encore trop souvent méconnues. Inspirée par les femmes remarquables que j'ai rencontrées en grandissant au Gabon, j'ai souhaité créer bien plus qu'un magazine numérique : un espace où les femmes peuvent s'inspirer mutuellement, tisser des liens et célébrer leurs réussites.",
        about_story2: "Réalisé dans le cadre de mon Portfolio Project à Holberton School, LIONESS allie ma passion pour le développement web à mon engagement en faveur de la valorisation du leadership féminin. Développée avec Django, Bootstrap, HTML, CSS et JavaScript, cette plateforme moderne est responsive, accessible et pensée pour offrir une expérience utilisateur de qualité.",
        project_links: "Liens du projet",
        live_app: "Application en ligne",
        github: "Dépôt GitHub",
        demo: "Vidéo de démonstration",
        navigation: "Navigation",
        portfolio: "Projet Portfolio",
        portfolio_desc: "Développé dans le cadre du Portfolio Project de Holberton School."
    }
};

function setLanguage(lang) {
    document.querySelectorAll("[data-i18n]").forEach(element => {
        const key = element.getAttribute("data-i18n");
        if (translations[lang] && translations[lang][key]) {
            element.innerHTML = translations[lang][key];
        }
    });

    localStorage.setItem("language", lang);

    const currentLangDiv = document.querySelector(".current-language");
    if (currentLangDiv) {
        currentLangDiv.innerHTML = lang.toUpperCase() + ' <i class="fa-solid fa-chevron-down ms-1 style-arrow"></i>';
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const lang = localStorage.getItem("language") || "en";
    setLanguage(lang);

    // Gestion de la fermeture automatique du menu mobile lors d'un clic
    document.querySelectorAll('#mobileMenu a').forEach(link => {
        link.addEventListener('click', () => {
            const menu = document.getElementById('mobileMenu');
            if (menu && typeof bootstrap !== 'undefined') {
                const bsCollapse = bootstrap.Collapse.getInstance(menu) || new bootstrap.Collapse(menu, { toggle: false });
                bsCollapse.hide();
            }
        });
    });
});
