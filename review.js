module.exports = [
    {
        _id: 'review:1',
        rating: 5,
        date: '2022-10-10',
        reviewText: 'Great book',
        user: {
            _id: 'user:1',
            username: 'username1',
            email: 'username1@email.com',
            password: 'password'
        },
        book: '6'
    },

    {
        _id: 'review:2',
        rating: 3,
        date: '2022-10-12',
        reviewText: 'Good book',
        user: {
            _id: 'user:2',
            username: 'username2',
            email: 'username2@email.com',
            password: 'password123'
        },
        book: '10'
    },

    {
        _id: 'review:3',
        rating: 3,
        date: '2022-10-10',
        reviewText: 'Amazing book',
        user: {
            _id: 'user:1',
            username: 'username1',
            email: 'username1@email.com',
            password: 'password'
        },
        book: '6'
    },

    {
        _id: 'review:4',
        rating: 5,
        date: '2022-10-15',
        reviewText: 'Great book',
        user: {
            _id: 'user:3',
            username: 'username3',
            email: 'username3@email.com',
            password: 'password'
        },
        book: '6'
    }
];