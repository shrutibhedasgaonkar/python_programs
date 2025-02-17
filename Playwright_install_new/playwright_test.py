import { test, expect } from '@playwright/test';

test('Should add item to cart and complete checkout', async ({ page }) => {
  // Navigate to the e-commerce site
  await page.goto('https://bstackdemo.com/');