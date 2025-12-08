import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: '13-Week Industry Course - From Fundamentals to Production',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://SufyanMem0n.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  baseUrl: '/Physical-AI-Humanoid-Robotics-Textbook/',

  // GitHub pages deployment config.
  organizationName: 'SufyanMem0n', // Usually your GitHub org/user name.
  projectName: 'Physical-AI-Humanoid-Robotics-Textbook', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          editUrl: 'https://github.com/SufyanMem0n/Physical-AI-Humanoid-Robotics-Textbook/edit/main/',
        },
        blog: false, // Optional: disable the blog plugin
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    navbar: {
      title: 'Physical AI Course',
      logo: {
        alt: 'Physical AI Course Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'courseSidebar',
          position: 'left',
          label: 'Course',
        },
        // As per the prompt, but there is no /docs/exercises yet. I will comment it out.
        // {to: '/docs/exercises', label: 'Exercises', position: 'left'},
        {
          href: 'https://github.com/SufyanMem0n/Physical-AI-Humanoid-Robotics-Textbook',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      copyright: `For Industry Practitioners | ${new Date().getFullYear()}`,
    },
    prism: {
      theme: prismThemes.vsDark,
      darkTheme: prismThemes.vsDark,
      additionalLanguages: ['python', 'bash', 'yaml', 'docker'],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
