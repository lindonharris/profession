# Lovable Prompt: Settings & Billing Page

**Phase:** 2 - Premium Tier
**Page:** Account Settings & Billing
**URL:** `/dashboard/settings`
**Build Order:** 7 of 7

---

## Copy-Paste This Into Lovable:

```
I need a settings and billing page where users manage their account. Think Stripe billing portal - clean tabs, clear subscription info, easy to update payment methods.

Use the same sidebar from other dashboard pages.

**Top of page:**
- "Settings" heading
- "Manage your account and billing" subheading

**Tab navigation:**
Use the Tabs component from shadcn/ui with 4 tabs: Profile, Billing, Notifications, Security

**Tab 1: Profile**

Section 1 - Personal Information:
- Profile picture with "Change Photo" button
- Full name (text input)
- Email (text input, but disabled - can't change email)
- Company name (optional text input)
- Time zone (dropdown)
- "Save Changes" button

Section 2 - Preferences:
- Language dropdown (English, Spanish, French, German)
- Date format dropdown (MM/DD/YYYY, DD/MM/YYYY, YYYY-MM-DD)
- Email digest frequency (Daily, Weekly, Monthly, Never)
- "Save Changes" button

**Tab 2: Billing**

Section 1 - Active Subscriptions:
Table showing all activated agents:
- Agent name with icon
- Tier badge (UTILITY or PREMIUM)
- Price per month
- Next billing date
- Actions (Pause, Upgrade/Downgrade, Cancel)

Show total monthly cost at bottom.

Section 2 - Payment Method:
Card showing:
- Credit card icon from Lucide React
- Masked card number (•••• •••• •••• 4242)
- Expiry date
- "Update" and "Remove" buttons

If no card on file, show "Add Payment Method" button.

Section 3 - Billing History:
Table of past invoices:
- Date
- Amount
- Status (Paid badge in green, Failed badge in red)
- Download PDF link

Show last 10 invoices with "View All →" link.

**Tab 3: Notifications**

Toggle switches for different notification types:
- Agent Activity Reports (Daily digest of all agent activity)
- Payment Reminders (Upcoming charges and failed payments)
- Feature Updates (New features and product updates)
- Security Alerts (Login from new device, password changes)
- Agent Errors (When an agent fails or needs attention)

Each has a label and description below.

**Tab 4: Security**

Section 1 - Password:
- "Change Password" button
- Shows when password was last changed

Section 2 - Two-Factor Authentication:
- Status (Enabled or Disabled)
- "Enable 2FA" or "Disable 2FA" button
- Description of what 2FA does

Section 3 - Sessions:
Table of active sessions:
- Device (Chrome on Mac, iPhone, etc.)
- Location (IP address or city)
- Last active time
- "Revoke" button for each session

Section 4 - Danger Zone:
Red-bordered card with:
- "Delete Account" button (destructive styling)
- Warning text about what happens when you delete

**Design notes:**
- Use Tabs component for navigation
- Use Card component for each section
- Use Table component from shadcn/ui
- Use Input, Select components for forms
- Toggle switches for notifications
- Icons from Lucide React (User, CreditCard, Bell, Shield, etc.)
- Keep the dark theme consistent
- Responsive - tables should scroll horizontally on mobile if needed
```

---

## Sample Data:

**Profile:**
- Name: John Doe
- Email: john@acme.com (can't be changed)
- Company: Acme Inc
- Time Zone: Pacific Time (US & Canada)

**Active Subscriptions:**
1. Expense Tracker - UTILITY - $69/month - Next billing: Oct 15
2. Email Sweeper - UTILITY - $29/month - Next billing: Oct 18
3. Invoice Chaser - PREMIUM - $100/month - Next billing: Oct 20

Total: $198/month

**Payment Method:**
Visa ending in 4242
Expires 12/2026

**Billing History:**
- Sep 1, 2025 | $198.00 | Paid | Download PDF
- Aug 1, 2025 | $128.00 | Paid | Download PDF
- Jul 1, 2025 | $69.00 | Paid | Download PDF

**Notification Preferences:**
- Agent Activity Reports: ON
- Payment Reminders: ON
- Feature Updates: ON
- Security Alerts: ON
- Agent Errors: ON

**Security:**
- Password last changed: 45 days ago
- Two-Factor Authentication: Enabled
- Active Sessions: 2 (Current session + iPhone)

---

## Next Step:

This is the last page! After Lovable generates this, you'll have all 7 pages of the marketplace built. Time to move to Task 2 (Supabase database setup).
