# Start with users that need to be verified,
# and an empty list to hold confirmed users
unconfirmed_user = ['alice', 'brian', 'cadace']
confirmed_users = []

# Verufy each user until there are no more unconfirmed users.
# Move each veryfied user into the list of confirmed users.
while unconfirmed_user:
    curren_user = unconfirmed_user.pop()
    print(f"Verified user: {curren_user.title()}")
    confirmed_users.append(curren_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
